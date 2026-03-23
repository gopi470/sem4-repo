rem drop tables

drop table Payment;
drop table Reservation;
drop table Tourist;
drop table Sailor;
drop table Boat;


rem create tables 
rem Boat
create table Boat(
  boat_id varchar(5) constraint pk_b primary key constraint chk_b_id check (boat_id like 'B%'),
  b_name varchar(20),
  b_type char(3) constraint chk_b_type check (b_type in ('car','lux','cru')),
  color char(10),
  max_cap number,
  price number
);


rem Boat data
insert into Boat values ('B001', 'Mark III', 'lux', 'blue', 30, 500);
insert into Boat values ('B002', 'Batcycle', 'cru', 'red', 25, 400);
insert into Boat values ('B003', 'Black Pearl', 'car', 'green', 15, 300);

rem Boat ID format violation
insert into Boat
values ('X001', ' WBoat', 'lux', 'blue', 10, 300);


rem violation in check type
insert into Boat values ('B004', 'Black Pearl', 'van', 'green', 15, 300);


rem primary key violation
insert into Boat values ('B001', 'Mark III', 'lux', 'blue', 30, 500);
 


rem Sailor
create table Sailor(
  S_id varchar(5) constraint pk_s primary key constraint chk_s_id check (S_id like 'S%'),
  S_name varchar(20),
  rating char(1) constraint chk_rating check (rating in ('A','B','C')),
  DOB date
);



rem Sailor data
insert into Sailor values ('S001', 'RDJ', 'A', date '1965-04-04');
insert into Sailor values ('S002', 'BAT MAN', 'B', date '1974-01-30');
insert into Sailor values ('S003', 'JACK S', 'B', date '1963-06-09');

rem violation on Sailor ID
insert into Sailor values ('D003', 'JACK S', 'B', date '1963-06-09');

rem Sailor rating violation
insert into Sailor
values ('S010', 'Mark', 'D', date '1992-05-10');


rem primary key violation
insert into Sailor values (null, 'RDJ', 'A', date '1965-04-04');
 


rem Tourist
create table Tourist(
  T_id varchar(5) constraint pk_t primary key  constraint chk_t_id check (T_id like 'T%'),
  T_name varchar(20),
  address varchar(20),
  DOB date,
  phone number(10) constraint phone_uq unique               
);



rem Tourist data
insert into Tourist values ('T001', 'Dustin', 'Mumbai', date '1987-11-10', 9876543211);  
insert into Tourist values ('T002', 'Mike', 'Chennai', date '1988-05-18', 8765432108);
insert into Tourist values ('T003', 'Will', 'Chennai', date '1990-07-22', 8765432109);

rem Tourist ID format violation
insert into Tourist
values  ('F003', 'Bill', 'Banglore', date '1994-12-22', 7765432109);


rem violation on phone number (unique)
insert into Tourist values ('T004', 'Hope', 'Chennai', date '1990-07-22', 8765432109);


rem Reservation
create table Reservation(
  To_id varchar(5) constraint to_fk references Tourist(T_id),
  R_id varchar(5) constraint r_pk primary key constraint chk_R_id check (R_id like 'R%'),
  Sailing_date date,
  S_id varchar(5) constraint sa_fk references Sailor(S_id),
  B_id varchar(5) constraint bo_fk references Boat(boat_id),
  R_date date,
  no_p number(2),
  no_C number(2),
  constraint chk_R_date check (Sailing_date >= R_date + 12),
  constraint chk_same_b_d unique (B_id,Sailing_date)
);


rem Reservation data
insert into Reservation
values ('T001','R001', date '2025-12-25', 'S001', 'B001',
        date '2025-12-10', 5, 2);

insert into Reservation
values ('T002','R002', date '2025-12-28', 'S002', 'B002',
        date '2025-12-12', 8, 1);


rem foreign key violation (sailor id not avail)
values ('T002','R002', date '2025-12-28', 'S009', 'B002',
        date '2025-12-12', 8, 1);


rem foreign key violation deleting parent table

delete from Boat where boat_id = 'B002';


rem Voilation on reservation id
insert into Reservation
values ('T001', 'Y005', date '2025-12-10', 'S001', 'B001', date '2025-10-12', 3, 1);


rem Violation Sailing date earlier than reservation date
insert into Reservation
values ('T001', 'R005', date '2025-12-10', 'S001', 'B001', date '2025-12-12', 3, 1);


rem violaion on register same boat on same data
insert into Reservation
values ('T004','R007', date '2025-12-28', 'S002', 'B002',
        date '2025-12-12', 8, 1);


rem Payment
create table Payment(
  payment_id varchar(5) constraint pk_P primary key constraint chk_P_id check (payment_id like 'P%'),
  res_id varchar(5) constraint rv_fk references Reservation(R_id),
  payment_date date,
  amount number(8,2),
  payment_mode varchar(10)
    constraint chk_mode check (payment_mode in ('Cash','Card','UPI','Online')),
  payment_status varchar(10)
);


rem Payment data
insert into Payment
values ('P001', 'R001', date '2025-12-25',
        25000.00,'Card', 'Paid');

insert into Payment
values ('P002', 'R002', date '2025-12-28',
        32000.00,'UPI', 'Paid');


rem violation on check payment id
insert into Payment
values ('L002', 'R002', date '2025-12-28',32000.00,'UPI', 'Paid');

rem violation on check payment mode
insert into Payment
values ('P003', 'R003', date '2026-12-28',32000.00,'loan', 'Paid');




rem Describe tables
describe Boat;
describe Sailor;
describe Tourist;
describe Reservation;
describe Payment;
