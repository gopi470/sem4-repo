set echo on;
set serveroutput on;
@ C:\Users\HP\Documents\Sem 4\dbms\t1.sql;

drop view Resv_Det;

rem 1.Ensure that total people (adults + children) do not exceed boat capacity before insert or 
rem update in reservation table. 
CREATE OR REPLACE TRIGGER trg_check_capacity
BEFORE INSERT OR UPDATE ON Reservation
FOR EACH ROW
DECLARE
    v_capacity Boat.capacity%TYPE;
    v_total_people NUMBER;
BEGIN
    -- Calculate total people
    v_total_people := :NEW.no_of_people + :NEW.no_of_children;

    -- Get boat capacity
    SELECT capacity
    INTO v_capacity
    FROM Boat
    WHERE boat_id = :NEW.boat_id;

    -- Check condition
    IF v_total_people > v_capacity THEN
        RAISE_APPLICATION_ERROR(-20001,
        'Total people exceed boat capacity');
    END IF;

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20002,
        'Boat not found');
END;
/

INSERT INTO RESERVATION VALUES ('R030','B002','S004','T004','05-JAN-2005','16-JAN-2005',6,8);  




rem 2.In the Boat Reservation Management System, tourists make reservations for boats on a 
rem particular date (resv_date) and specify the date on which they intend to sail (sail_date). 
rem According to the business policy: A sail date cannot be earlier than the reservation date. 

CREATE OR REPLACE TRIGGER trg_check_dates
BEFORE INSERT OR UPDATE ON Reservation
FOR EACH ROW
BEGIN
    IF :NEW.sail_date < :NEW.resv_date THEN
        RAISE_APPLICATION_ERROR(-20003,
        'Sail date cannot be earlier than reservation date');
    END IF;
END;
/

INSERT INTO RESERVATION VALUES ('R030','B002','S004','T004','24-JAN-2005','16-JAN-2005',1,2);  



rem 3.In the Boat Reservation Management System, every reservation must be paid before it 
rem is considered valid. When a payment is successfully completed (p_status = 
rem 'SUCCESS'), the system must automatically update the corresponding reservation 
rem record to indicate that it is confirmed. If payment fails or is pending, the reservation 
rem should remain unconfirmed. 

rem 4. A reservation should be marked as CONFIRMED only if: 
rem Total successful payments for that reservation are greater than or equal to boat price × number of people 
rem If total successful payment is less than required amount → status remains PENDING 
rem If payment status becomes FAILED → reservation should not be confirmed.

ALTER TRIGGER trg_check_capacity DISABLE;
ALTER TRIGGER trg_check_dates DISABLE;


ALTER TABLE RESERVATION
ADD status VARCHAR2(15) DEFAULT 'PENDING';

CREATE OR REPLACE TRIGGER trg_payment_validation
AFTER INSERT OR UPDATE ON payment
DECLARE
    v_total_paid     NUMBER;
    v_price          boat.price%TYPE;
    v_total_people   NUMBER;
    v_required_amt   NUMBER;
BEGIN

    FOR rec IN (SELECT DISTINCT resv_id FROM payment)
    LOOP

        SELECT b.price,
               (r.no_of_people + r.no_of_children)
        INTO v_price, v_total_people
        FROM reservation r
        JOIN boat b
        ON r.boat_id = b.boat_id
        WHERE r.resv_id = rec.resv_id;

        v_required_amt := v_price * v_total_people;

        SELECT NVL(SUM(amount),0)
        INTO v_total_paid
        FROM payment
        WHERE resv_id = rec.resv_id
        AND p_status = 'SUCCESS';

        IF v_total_paid >= v_required_amt THEN
            UPDATE reservation
            SET status = 'CONFIRMED'
            WHERE resv_id = rec.resv_id;
        ELSE
            UPDATE reservation
            SET status = 'PENDING'
            WHERE resv_id = rec.resv_id;
        END IF;

    END LOOP;

END;
/

REM Insert validation

INSERT INTO reservation
VALUES ('R030','B008','S002','T006','06-APR-2006','10-APR-2006',6,1,'PENDING');

INSERT INTO payment
VALUES ('P030','R030',1000,SYSDATE,'UPI','SUCCESS');

SELECT resv_id, status
FROM reservation
WHERE resv_id = 'R030';

INSERT INTO payment
VALUES ('P031','R030',2000,SYSDATE,'CARD','SUCCESS');

SELECT resv_id, status
FROM reservation
WHERE resv_id = 'R030';

REM Update validation

UPDATE payment
SET p_status = 'FAILED'
WHERE p_id = 'P031';

SELECT resv_id, status
FROM reservation
WHERE resv_id = 'R030';


rem 5. In the Boat Reservation Management System, management wants to allow users to 
rem insert reservation details through a view instead of directly inserting into base tables. 
rem When a user inserts a record into the Reservation_Details view. Write an INSTEAD 
rem OF INSERT trigger to insert data into the Reservation table whenever a record is 
rem inserted into the view. The reservation status should be set to 'PENDING' by default. 

CREATE OR REPLACE VIEW reservation_details_view AS
SELECT r.resv_id,r.boat_id,r.sailor_id,r.tourist_id,r.resv_date,r.sail_date,r.no_of_people,r.no_of_children
FROM reservation r;

CREATE OR REPLACE TRIGGER trg_reservation_details_insert
INSTEAD OF INSERT ON reservation_details_view
FOR EACH ROW
BEGIN
    INSERT INTO reservation (resv_id,boat_id,sailor_id,tourist_id,resv_date,sail_date,no_of_people,no_of_children,status)
    VALUES (:NEW.resv_id,:NEW.boat_id,:NEW.sailor_id,:NEW.tourist_id,:NEW.resv_date,:NEW.sail_date,:NEW.no_of_people,:NEW.no_of_children,'PENDING');
END;
/

REM Insert validation

INSERT INTO reservation_details_view
VALUES ('R050','B003','S003','T003','19-MAY-2006','15-APR-2005',3,1);

SELECT resv_id, status
FROM reservation
WHERE resv_id = 'R050';

Select *
from reservation_details_view;