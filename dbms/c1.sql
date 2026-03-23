DROP TABLE payment;
DROP TABLE reservation;
DROP TABLE tourist;
DROP TABLE sailor;
DROP TABLE boat;

REM Create Tables

create table boat(
boat_id varchar2(4) constraint bid_pk primary key constraint bid_b check (boat_id like 'B%'),
boat_name varchar2(20),
type varchar2(3) constraint boat_type check(type in ('LUX','CAR','CRU')),
capacity number(4),
price number(6),
color varchar2(10));


create table sailor(
sailor_id varchar2(4) constraint sid_pk primary key constraint sid_s check (sailor_id like 'S%'),
sailor_name varchar2(10),
rating varchar(2) constraint rating_abc check (rating in ('A','B','C')),
sailor_dob date);


create table tourist(
tourist_id varchar2(4) constraint tid_pk primary key constraint tid_t check (tourist_id like 'T%'),
tourist_name varchar2(10),
address varchar2(20),
phone number(10) constraint ph_uni unique );


CREATE TABLE RESERVATION(
RESV_ID VARCHAR2(5) CONSTRAINT RESV_PK PRIMARY KEY CONSTRAINT RESV_CHK CHECK(RESV_ID LIKE 'R%'),
BOAT_ID VARCHAR2(5) CONSTRAINT BID_FK REFERENCES BOAT(BOAT_ID) ON DELETE CASCADE,
SAILOR_ID VARCHAR2(5) CONSTRAINT SID_FK REFERENCES SAILOR(SAILOR_ID) ON DELETE CASCADE,
TOURIST_ID VARCHAR2(5) CONSTRAINT TID_FK REFERENCES TOURIST(TOURIST_ID) ON DELETE CASCADE,
RESV_DATE DATE ,
SAIL_DATE DATE CONSTRAINT SDATE_NN NOT NULL,
NO_OF_PEOPLE NUMBER(3),
NO_OF_CHILDREN NUMBER(3),
CONSTRAINT ADVBOOK_CHK CHECK(SAIL_DATE <= RESV_DATE+12),
CONSTRAINT UNI_BOOK UNIQUE(BOAT_ID, SAILOR_ID,SAIL_DATE)
);

create table payment(
p_id varchar2(4) constraint pid_pk primary key constraint pid_c check (p_id like 'P%'),
resv_id varchar2(4) constraint rid_fk references reservation(resv_id),
amount decimal(10,2),
p_date DATE,
p_mode varchar2(10),
p_status varchar2(10));


REM Populate Tables


INSERT INTO BOAT VALUES ('B001','Sea Queen','LUX',10,500.00,'White');
INSERT INTO BOAT VALUES ('B002','Ocean Rider','CAR',12,350.00,'Blue');
INSERT INTO BOAT VALUES ('B003','Wave King','CRU',20,450.00,'Red');
INSERT INTO BOAT VALUES ('B004','Pearl Boat','LUX',8,600.00,'White');
INSERT INTO BOAT VALUES ('B005','Blue Dolphin','CAR',15,300.00,'Blue');
INSERT INTO BOAT VALUES ('B006','Sun Cruiser','CRU',25,550.00,'Yellow');
INSERT INTO BOAT VALUES ('B007','Aqua Star','LUX',6,650.00,'Silver');
INSERT INTO BOAT VALUES ('B008','River Queen','CAR',14,320.00,'Green');
INSERT INTO BOAT VALUES ('B009','Sea Breeze','CRU',18,480.00,'Sky Blue');
INSERT INTO BOAT VALUES ('B010','Golden Wave','LUX',10,700.00,'Gold');
INSERT INTO BOAT VALUES ('B011','Coral Rider','CAR',16,340.00,'Orange');
INSERT INTO BOAT VALUES ('B012','Deep Blue','CRU',22,520.00,'Navy');
INSERT INTO BOAT VALUES ('B013','Marine Star','LUX',9,680.00,'White');
INSERT INTO BOAT VALUES ('B014','Lagoon Boat','CAR',13,310.00,'Teal');
INSERT INTO BOAT VALUES ('B015','Royal Cruise','CRU',30,750.00,'Black');
INSERT INTO BOAT VALUES ('B016','Wave Runner','LUX',7,620.00,'Red');
INSERT INTO BOAT VALUES ('B017','Sea Horse','CAR',11,330.00,'Brown');
INSERT INTO BOAT VALUES ('B018','Blue Pearl','CRU',24,580.00,'Blue');
INSERT INTO BOAT VALUES ('B019','Ocean Dream','LUX',8,660.00,'Purple');
INSERT INTO BOAT VALUES ('B020','Island Cruiser','CRU',28,700.00,'Grey');



INSERT INTO SAILOR VALUES ('S001','Arun','A','12-MAY-1990');
INSERT INTO SAILOR VALUES ('S002','Bala','B','23-NOV-1988');
INSERT INTO SAILOR VALUES ('S003','Karthik','C','18-MAR-1992');
INSERT INTO SAILOR VALUES ('S004','Bala','A','09-JUL-1987');
INSERT INTO SAILOR VALUES ('S005','Suresh','B','25-JAN-1991');
INSERT INTO SAILOR VALUES ('S006','Ramesh','C','14-SEP-1989');
INSERT INTO SAILOR VALUES ('S007','Vijay','A','05-DEC-1993');
INSERT INTO SAILOR VALUES ('S009','Manoj','B','21-AUG-1990');
INSERT INTO SAILOR VALUES ('S010','Bala','C','11-APR-1994');
INSERT INTO SAILOR VALUES ('S011','Ravi','A','17-FEB-1986');
INSERT INTO SAILOR VALUES ('S012','Kumar','B','08-OCT-1992');
INSERT INTO SAILOR VALUES ('S014','Mahesh','C','03-JUN-1991');
INSERT INTO SAILOR VALUES ('S015','Naveen','A','27-SEP-1995');
INSERT INTO SAILOR VALUES ('S016','Gokul','B','14-DEC-1988');
INSERT INTO SAILOR VALUES ('S017','Surya','C','22-MAY-1993');
INSERT INTO SAILOR VALUES ('S019','Harish','B','29-JUL-1990');
INSERT INTO SAILOR VALUES ('S020','Kiran','A','02-NOV-1996');

   


INSERT INTO TOURIST VALUES ('T001','Anitha','Chennai','9876543210');
INSERT INTO TOURIST VALUES ('T002','Rajesh','Coimbatore','9876543211');
INSERT INTO TOURIST VALUES ('T003','Meena','Madurai','9876543212');
INSERT INTO TOURIST VALUES ('T004','Suresh','Trichy','9876543213');
INSERT INTO TOURIST VALUES ('T005','Priya','Salem','9876543214');
INSERT INTO TOURIST VALUES ('T006','Karthika','Erode','9876543215');
INSERT INTO TOURIST VALUES ('T007','Vignesh','Vellore','9876543216');
INSERT INTO TOURIST VALUES ('T008','Lakshmi','Tirunelveli','9876543217');
INSERT INTO TOURIST VALUES ('T009','Aravind','Thanjavur','9876543218');
INSERT INTO TOURIST VALUES ('T010','Divya','Thoothukudi','9876543219');
INSERT INTO TOURIST VALUES ('T011','Mohan','Karur','9876543220');
INSERT INTO TOURIST VALUES ('T012','Revathi','Namakkal','9876543221');
INSERT INTO TOURIST VALUES ('T013','Balaji','Kanchipuram','9876543222');
INSERT INTO TOURIST VALUES ('T014','Sandhya','Cuddalore','9876543223');
INSERT INTO TOURIST VALUES ('T015','Ganesh','Tiruvallur','9876543224');
INSERT INTO TOURIST VALUES ('T016','Nithya','Ramanathapuram','9876543225');
INSERT INTO TOURIST VALUES ('T017','Prabhu','Dharmapuri','9876543226');
INSERT INTO TOURIST VALUES ('T018','Keerthi','Dindigul','9876543227');
INSERT INTO TOURIST VALUES ('T019','Sathish','Virudhunagar','9876543228');
INSERT INTO TOURIST VALUES ('T020','Janani','Chengalpattu','9876543229');





INSERT INTO RESERVATION VALUES ('R001','B001','S001','T001','05-JAN-2005','10-JAN-2005',4,1);  
INSERT INTO RESERVATION VALUES ('R002','B001','S003','T002','05-JAN-2005','12-JAN-2005',6,2);  
INSERT INTO RESERVATION VALUES ('R003','B002','S002','T003','05-JAN-2005','15-JAN-2005',5,0);  
INSERT INTO RESERVATION VALUES ('R004','B002','S004','T004','05-JAN-2005','16-JAN-2005',3,1);  
INSERT INTO RESERVATION VALUES ('R005','B001','S005','T005','15-JAN-2005','22-JAN-2005',7,2);  
INSERT INTO RESERVATION VALUES ('R006','B002','S006','T006','15-JAN-2005','25-JAN-2005',10,3); 
INSERT INTO RESERVATION VALUES ('R007','B001','S001','T001','01-FEB-2005','08-FEB-2005',2,0);  
INSERT INTO RESERVATION VALUES ('R008','B004','S001','T007','01-FEB-2005','10-FEB-2005',8,1);  
INSERT INTO RESERVATION VALUES ('R009','B003','S007','T008','05-FEB-2005','12-FEB-2005',4,1);
INSERT INTO RESERVATION VALUES ('R010','B004','S007','T008','10-FEB-2005','18-FEB-2005',9,2);
INSERT INTO RESERVATION VALUES ('R011','B006','S009','T010','18-FEB-2005','28-FEB-2005',6,3);
INSERT INTO RESERVATION VALUES ('R012','B002','S010','T001','01-MAR-2005','08-MAR-2005',11,4); 
INSERT INTO RESERVATION VALUES ('R013','B008','S011','T002','01-MAR-2005','12-MAR-2005',3,0);
INSERT INTO RESERVATION VALUES ('R014','B009','S012','T003','10-MAR-2005','17-MAR-2005',7,1);
INSERT INTO RESERVATION VALUES ('R015','B009','S014','T004','15-MAR-2005','17-MAR-2005',5,2);
INSERT INTO RESERVATION VALUES ('R016','B011','S014','T005','20-MAR-2005','18-MAR-2005',12,3);
INSERT INTO RESERVATION VALUES ('R017','B012','S015','T006','25-MAR-2005','31-MAR-2005',4,1);
INSERT INTO RESERVATION VALUES ('R018','B013','S016','T007','01-MAR-2005','10-MAR-2005',8,2);
INSERT INTO RESERVATION VALUES ('R019','B014','S017','T008','05-MAR-2005','15-MAR-2005',6,0);
INSERT INTO RESERVATION VALUES ('R020','B003','S017','T001','10-MAR-2005','20-MAR-2005',9,3);
INSERT INTO RESERVATION VALUES ('R021','B016','S019','T010','15-MAR-2005','25-MAR-2005',2,1);
INSERT INTO RESERVATION VALUES ('R022','B017','S020','T010','20-MAR-2005','28-MAR-2005',10,2);
INSERT INTO RESERVATION VALUES ('R023','B018','S001','T010','25-MAR-2005','31-MAR-2005',7,4); 
INSERT INTO RESERVATION VALUES ('R024','B019','S002','T002','01-MAR-2005','12-MAR-2005',5,1);
INSERT INTO RESERVATION VALUES ('R025','B020','S003','T007','01-MAR-2005','09-MAR-2005',11,2);




INSERT INTO PAYMENT VALUES ('P001','R001',2000,'01-JAN-2025','CASH','PAID');
INSERT INTO PAYMENT VALUES ('P002','R002',2100,'02-JAN-2025','CARD','PAID');
INSERT INTO PAYMENT VALUES ('P003','R003',2250,'03-JAN-2025','UPI','PAID');
INSERT INTO PAYMENT VALUES ('P004','R004',1800,'04-JAN-2025','ONLINE','PAID');
INSERT INTO PAYMENT VALUES ('P005','R005',2450,'05-JAN-2025','CASH','PAID');
INSERT INTO PAYMENT VALUES ('P006','R006',5000,'06-JAN-2025','CARD','PAID');
INSERT INTO PAYMENT VALUES ('P007','R007',1300,'07-JAN-2025','UPI','PAID');
INSERT INTO PAYMENT VALUES ('P008','R008',2400,'08-JAN-2025','ONLINE','PAID');
INSERT INTO PAYMENT VALUES ('P009','R009',3800,'09-JAN-2025','CASH','PAID');
INSERT INTO PAYMENT VALUES ('P010','R010',2800,'10-JAN-2025','CARD','PAID');
INSERT INTO PAYMENT VALUES ('P011','R011',4500,'11-JAN-2025','UPI','PAID');
INSERT INTO PAYMENT VALUES ('P012','R012',2600,'12-JAN-2025','ONLINE','PENDING');
INSERT INTO PAYMENT VALUES ('P013','R013',3000,'13-JAN-2025','CASH','PAID');
INSERT INTO PAYMENT VALUES ('P014','R014',1500,'14-JAN-2025','CARD','CANCELLED');
INSERT INTO PAYMENT VALUES ('P015','R015',9000,'15-JAN-2025','UPI','PAID');
INSERT INTO PAYMENT VALUES ('P016','R016',2600,'16-JAN-2025','ONLINE','PAID');
INSERT INTO PAYMENT VALUES ('P017','R017',3200,'17-JAN-2025','CASH','PAID');
INSERT INTO PAYMENT VALUES ('P018','R018',4800,'18-JAN-2025','CARD','REFUNDED');
INSERT INTO PAYMENT VALUES ('P019','R019',2750,'19-JAN-2025','UPI','PAID');
INSERT INTO PAYMENT VALUES ('P020','R020',7700,'20-JAN-2025','ONLINE','PAID');



REM SUBQUERIES

REM 1. Display distinct boats reserved in the same month as SYSDATE
SELECT DISTINCT *
FROM boat
WHERE boat_id IN (
    SELECT boat_id
    FROM reservation
    WHERE TO_CHAR(sail_date,'MM') = TO_CHAR(SYSDATE,'MM')
);

REM 2. Display tourists whose sail date is the last day of a month
SELECT DISTINCT tourist_id, tourist_name
FROM tourist
WHERE tourist_id IN (
    SELECT tourist_id
    FROM reservation
    WHERE sail_date = LAST_DAY(sail_date)
);

REM 3. Display boats that have never been reserved
SELECT *
FROM boat
WHERE boat_id NOT IN (
    SELECT boat_id FROM reservation
);

REM 4. Display tourists who made more than one reservation on same date
SELECT tourist_id, tourist_name
FROM tourist
WHERE tourist_id IN (
    SELECT tourist_id
    FROM reservation
    GROUP BY tourist_id, resv_date
    HAVING COUNT(resv_id) > 1
);

REM 5. Display boats reserved by maximum number of tourist use ALL
SELECT *
FROM boat
WHERE boat_id IN (
    SELECT boat_id
    FROM reservation
    GROUP BY boat_id
    HAVING COUNT(DISTINCT tourist_id) >= ALL (
        SELECT COUNT(DISTINCT tourist_id)
        FROM reservation
        GROUP BY boat_id
    )
);

REM 6. List tourist IDs who reserved boats costing more than average price
SELECT DISTINCT tourist_id
FROM reservation
WHERE boat_id IN (
    SELECT boat_id
    FROM boat
    WHERE price > (SELECT AVG(price) FROM boat)
);

REM — JOINS

REM 1. Average payment earned by sailors grouped by rating (Only PAID)
SELECT s.rating, AVG(p.amount) AS avg_amount
FROM sailor s
JOIN reservation r ON s.sailor_id = r.sailor_id
JOIN payment p ON r.resv_id = p.resv_id
WHERE p.p_status = 'PAID'
GROUP BY s.rating;

REM 2. Boats reserved by T001 where T001 paid more than any other tourist
SELECT b.boat_id, b.boat_name, SUM(p.amount) AS total_paid
FROM boat b
JOIN reservation r ON b.boat_id = r.boat_id
JOIN payment p ON r.resv_id = p.resv_id
WHERE r.tourist_id = 'T001'
AND p.p_status = 'PAID'
GROUP BY b.boat_id, b.boat_name
HAVING SUM(p.amount) > (
    SELECT MAX(p2.amount)
    FROM payment p2
    JOIN reservation r2 ON p2.resv_id = r2.resv_id
    WHERE r2.boat_id = b.boat_id
);

REM 3. Details of boat reserved by least number of tourists
SELECT t.*, r.resv_id, b.boat_name
FROM tourist t
JOIN reservation r ON t.tourist_id = r.tourist_id
JOIN boat b ON r.boat_id = b.boat_id
WHERE b.boat_id IN (
    SELECT boat_id
    FROM reservation
    GROUP BY boat_id
    HAVING COUNT(DISTINCT tourist_id) <= ALL (
        SELECT COUNT(DISTINCT tourist_id)
        FROM reservation
        GROUP BY boat_id
    )
);

REM 4. Tourists who reserved all three boat types (LUX, CAR, CRU)
SELECT DISTINCT t.tourist_id, t.tourist_name, r.resv_id
FROM tourist t
JOIN reservation r ON t.tourist_id = r.tourist_id
JOIN boat b ON r.boat_id = b.boat_id
WHERE t.tourist_id IN (
    SELECT r2.tourist_id
    FROM reservation r2
    JOIN boat b2 ON r2.boat_id = b2.boat_id
    GROUP BY r2.tourist_id
    HAVING COUNT(DISTINCT b2.type) = 3
);

REM 5. Display all boats with reservation details (including unreserved boats)
SELECT b.*, r.*
FROM boat b
LEFT OUTER JOIN reservation r
ON b.boat_id = r.boat_id;

REM 6. Tourists whose reservation count is greater than average (Correlated)
SELECT t.tourist_id, t.tourist_name
FROM tourist t
WHERE (
    SELECT COUNT(*)
    FROM reservation r
    WHERE r.tourist_id = t.tourist_id
) >
(
    SELECT AVG(cnt)
    FROM (
        SELECT COUNT(*) cnt
        FROM reservation
        GROUP BY tourist_id
    )
);

REM SET OPERATIONS

REM 1. Boat IDs which are reserved OR priced above average
SELECT boat_id FROM reservation
UNION
SELECT boat_id FROM boat
WHERE price > (SELECT AVG(price) FROM boat);

REM 2. Tourists who have not made any reservation
SELECT tourist_id, tourist_name FROM tourist
MINUS
SELECT t.tourist_id, t.tourist_name
FROM tourist t
JOIN reservation r ON t.tourist_id = r.tourist_id;

REM 3. Boats having same color as both LUX and CRU boats
SELECT *
FROM boat
WHERE color IN (
    SELECT color FROM boat WHERE type = 'LUX'
    INTERSECT
    SELECT color FROM boat WHERE type = 'CRU'
);















