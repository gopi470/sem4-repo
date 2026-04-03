rem alter 


rem 10. Number of children must be mentioned
desc Reservation;
alter table Reservation
modify no_C number(2) not null;
desc Reservation;

rem no mention the no of child
insert into Reservation
values ('T001','R001', date '2025-12-25', 'S001', 'B001',
        date '2025-12-10', 5,null);



rem 11. Rename phone to contact_number
desc Tourist;
alter table Tourist
rename column phone to contact_number;
desc Tourist;



rem 12. Increase width of tourist name
desc Tourist;

alter table Tourist
modify T_name varchar(50);
desc Tourist;



rem 13. Remove DOB from Tourist
desc Tourist;
alter table Tourist
drop column DOB;
desc Tourist;


rem ADD value for DOB After Dropping DOB column
insert into Tourist values ('T004', 'LEO', 'Chennai', date '1990-07-22', 8065432109);



rem 14. Reservation cannot be made without reserve date

alter table Reservation
modify R_date date not null;

rem After Constraint not null

insert into Reservation
values ('T002','R004', date '2025-12-31', 'S002', 'B002',
        null, 6, 2);



rem 15. Add Sailor rating 'D'
rem Before Adding new rating
insert into Sailor
values ('S004', 'Mark', 'D', date '1992-05-10');

alter table Sailor
drop constraint chk_rating;

alter table Sailor
add constraint chk_rating
check (rating in ('A','B','C','D'));

rem After Adding new rating
insert into Sailor
values ('S004', 'Mark', 'D', date '1992-05-10');



rem 16. On reservation delete, payment reference set to NULL


delete from reservation where R_id = 'R001';



alter table Payment drop constraint rv_fk;
alter table Payment add constraint rv_fk
foreign key (res_id) references Reservation(R_id) on delete set null;

rem Before Delete
select * from payment;

delete from reservation where R_id = 'R001';
rem Delete reservation R001
select * from payment;



rem 17. Cascade on Delete boatid,sailorid - reservation 


delete from Boat where boat_id = 'B002';



alter table reservation drop constraint sa_fk;
alter table reservation add constraint sa_fk
foreign key (S_id) references Sailor(S_id) on delete cascade;

alter table reservation drop constraint bo_fk;
alter table reservation add constraint bo_fk
foreign key (B_id) references Boat(boat_id) on delete cascade;


rem data before delete on cascade (boat id)
select * from reservation;

delete from Boat where boat_id = 'B002';

rem data after delete on cascade
select * from reservation;



rem 18. payment status values check

alter table Payment
add constraint chk_status_s
check (payment_status in ('Paid','Pending','Cancelled','Refunded'));

rem After adding constraint check payment_status
insert into Payment
values ('P004', 'R002', date '2025-12-28',
        19000.00,'UPI', 'Processing');



