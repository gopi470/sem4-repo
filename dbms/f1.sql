@ C:\Users\HP\Documents\dbms\z1.sql;

SET ECHO ON;
SET SERVEROUTPUT ON;

set serveroutput on;

DROP TRIGGER trg_check_capacity;
DROP TRIGGER trg_check_sail_date;
DROP TRIGGER trg_payment_success;
DROP TRIGGER trg_payment_confirm;
DROP TRIGGER trg_instead_insert;

ALTER TABLE reservation ADD status VARCHAR2(20) DEFAULT 'PENDING';




Rem 1. Ensure that total people (adults + children) do not exceed boat capacity before insert or update in reservation table.


CREATE OR REPLACE TRIGGER trg_check_capacity
BEFORE INSERT OR UPDATE OF boat_id, no_of_people, no_of_children
ON reservation
FOR EACH ROW
DECLARE
    v_capacity boat.capacity%TYPE;
BEGIN
    SELECT capacity INTO v_capacity
    FROM boat
    WHERE boat_id = :NEW.boat_id;

    IF NVL(:NEW.no_of_people,0) + NVL(:NEW.no_of_children,0) > v_capacity THEN
        RAISE_APPLICATION_ERROR(-20001,'Total people exceed boat capacity');
    END IF;
END;

/
show errors;

Rem Demo Q1 

INSERT INTO boat VALUES('B60','SEA','LUX',5,1000,'WHITE');
INSERT INTO sailor VALUES('S60','RAJ','A',DATE '2000-01-01');
INSERT INTO tourist VALUES('T60','KUMAR','CHENNAI',2222222222);

INSERT INTO reservation
VALUES('R60','B60','S60','T60',SYSDATE,SYSDATE+1,3,1,'PENDING');




Rem 2. In the Boat Reservation Management System, a sail date cannot be earlier than the reservation date.


CREATE OR REPLACE TRIGGER trg_check_sail_date
BEFORE INSERT OR UPDATE OF sail_date, resv_date
ON reservation
FOR EACH ROW
BEGIN
    IF :NEW.sail_date < :NEW.resv_date THEN
        RAISE_APPLICATION_ERROR(-20002,'Sail date cannot be earlier than reservation date');
    END IF;
END;
/
show errors;


Rem Demo Q2 

INSERT INTO reservation
VALUES('R61','B60','S60','T60',SYSDATE,SYSDATE+2,2,1,'PENDING');



Rem 3. When a payment is successfully completed (p_status = 'SUCCESS'), the system must automatically update the corresponding reservation record to indicate that it is confirmed.


CREATE OR REPLACE TRIGGER trg_payment_success
AFTER INSERT OR UPDATE OF p_status ON payment
FOR EACH ROW
BEGIN
    IF :NEW.p_status = 'SUCCESS' THEN
        UPDATE reservation
        SET status = 'PAID'
        WHERE resv_id = :NEW.resv_id;
    END IF;
END;
/
show errors;

Rem Demo Q3 

INSERT INTO reservation
VALUES('R62','B60','S60','T60',SYSDATE,SYSDATE+3,2,0,'PENDING');

INSERT INTO payment VALUES('P60','R62',1000,SYSDATE,'ONLINE','SUCCESS');

SELECT resv_id,status FROM reservation WHERE resv_id='R62';




Rem 4. A reservation should be marked as CONFIRMED only if total successful payments for that reservation are greater than or equal to boat price × number of people. If total successful payment is less than required amount → status remains PENDING.

CREATE OR REPLACE TRIGGER trg_payment_confirm
AFTER INSERT OR UPDATE ON payment
DECLARE
    v_total_paid NUMBER;
    v_price      NUMBER;
    v_people     NUMBER;
BEGIN
    FOR r IN (SELECT DISTINCT resv_id FROM payment)
    LOOP

        
        SELECT NVL(SUM(amount),0)
        INTO v_total_paid
        FROM payment
        WHERE resv_id = r.resv_id
        AND p_status = 'SUCCESS';

        SELECT b.price,
               (NVL(res.no_of_people,0) + NVL(res.no_of_children,0))
        INTO v_price, v_people
        FROM reservation res
        JOIN boat b ON res.boat_id = b.boat_id
        WHERE res.resv_id = r.resv_id;

        IF v_total_paid >= v_price * v_people THEN
            UPDATE reservation
            SET status = 'CONFIRMED'
            WHERE resv_id = r.resv_id;
        ELSE
            UPDATE reservation
            SET status = 'PENDING'
            WHERE resv_id = r.resv_id;
        END IF;

    END LOOP;
END;
/
show errors;

Rem Demo Q4 

INSERT INTO reservation
VALUES('R63','B60','S60','T60',SYSDATE,SYSDATE+4,2,0,'PENDING');

INSERT INTO payment VALUES('P61','R63',1000,SYSDATE,'ONLINE','SUCCESS');
SELECT resv_id,status FROM reservation WHERE resv_id='R63';

INSERT INTO payment VALUES('P62','R63',1000,SYSDATE,'ONLINE','SUCCESS');
SELECT resv_id,status FROM reservation WHERE resv_id='R63';


Rem 5. Write an INSTEAD OF INSERT trigger to insert data into the Reservation table whenever a record is inserted into the Reservation_Details view. The reservation status should be set to 'PENDING' by default.


CREATE OR REPLACE VIEW reservation_details AS
SELECT resv_id, boat_id, sailor_id, tourist_id,
       resv_date, sail_date,
       no_of_people, no_of_children
FROM reservation;

CREATE OR REPLACE TRIGGER trg_instead_insert
INSTEAD OF INSERT ON reservation_details
FOR EACH ROW
BEGIN
    INSERT INTO reservation(
        resv_id, boat_id, sailor_id, tourist_id,
        resv_date, sail_date,
        no_of_people, no_of_children, status
    )
    VALUES(
        :NEW.resv_id, :NEW.boat_id, :NEW.sailor_id, :NEW.tourist_id,
        :NEW.resv_date, :NEW.sail_date,
        :NEW.no_of_people, :NEW.no_of_children,
        'PENDING'
    );
END;
/
show errors;

Rem Demo Q5 

INSERT INTO reservation_details
VALUES('R64','B60','S60','T60',SYSDATE,SYSDATE+5,1,1);

SELECT resv_id,status FROM reservation WHERE resv_id='R64';