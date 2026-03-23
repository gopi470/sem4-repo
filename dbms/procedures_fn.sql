
set serveroutput on;
set echo on;


rem 1. check whether a boat of a given type and colour is available. if available print the details if not display message

CREATE OR REPLACE PROCEDURE pro_name
IS
   CURSOR c1 IS SELECT boat_id, boat_name, color FROM boat
      WHERE type = 'LUX' AND color = 'White';
    v_found BOOLEAN := FALSE;
BEGIN
   FOR i IN c1 LOOP
      v_found := TRUE;
      DBMS_OUTPUT.PUT_LINE(
         i.boat_id || ' ' || i.boat_name || ' ' || i.color
      );
   END LOOP;
   IF v_found = FALSE THEN
      DBMS_OUTPUT.PUT_LINE('Boat not available');
   END IF;
END;
/

exec pro_name;

rem 2. find number of people who sailed on a given date. if data not available display message

  declare
    cursor c2 is select * from RESERvation where SAIL_DATE='10-JAN-2005';
    num1 number:=0;
    v_found BOOLEAN := FALSE;
    begin
       for i in c2 loop
               num1:=num1+i.NO_OF_PEOPLE+i.no_of_children;
               v_found := TRUE;
       end loop;
    if v_found then
        if num1=0 then
            dbms_output.put_line('no sailing on this date');
        else
            dbms_output.put_line('total people sailed '||num1);
        end if;
    else
        dbms_output.put_line('data not available');
    end if;
end;
/

rem 3. procedure that takes reservation id and displays tourist, boat, sailor, adults, children and total passengers

create or replace procedure resv_details(R_rid in reservation.resv_id%type) is

    cursor c1 is
        select t.tourist_name, b.boat_name, b.type,
               s.sailor_name, r.no_of_people, r.no_of_children
        from reservation r, tourist t, boat b, sailor s
        where r.tourist_id=t.tourist_id
        and r.boat_id=b.boat_id
        and r.sailor_id=s.sailor_id
        and r.resv_id=R_rid;

    v_tname tourist.tourist_name%type;
    v_bname boat.boat_name%type;
    v_type boat.type%type;
    v_sname sailor.sailor_name%type;
    v_adult number;
    v_child number;
    v_total number;

begin
    open c1;
    fetch c1 into v_tname, v_bname, v_type, v_sname, v_adult, v_child;

    if c1%notfound then
        dbms_output.put_line('reservation not found');
    else
        v_total := v_adult + v_child;
        dbms_output.put_line('tourist '||v_tname);
        dbms_output.put_line('boat '||v_bname||' type '||v_type);
        dbms_output.put_line('sailor '||v_sname);
        dbms_output.put_line('adults '||v_adult||' children '||v_child);
        dbms_output.put_line('total passengers '||v_total);
    end if;

    close c1;
end;
/

exec resv_details('R014');


rem 4. procedure to generate formatted boat trip bill, apply discount and update payment

create or replace procedure generate_bill(R_rid in reservation.resv_id%type) is

    v_tname tourist.tourist_name%type;
    v_bname boat.boat_name%type;
    v_type boat.type%type;
    v_sname sailor.sailor_name%type;
    v_price boat.price%type;
    v_adult number;
    v_child number;
    v_total number;
    v_discount number:=0;
    v_final number;
    v_pid payment.resv_id%type;

begin
    select t.tourist_name, b.boat_name, b.type,
           s.sailor_name, b.price,
           r.no_of_people, r.no_of_children, p.resv_id
    into v_tname, v_bname, v_type,
         v_sname, v_price,
         v_adult, v_child, v_pid
    from reservation r, tourist t, boat b, sailor s, payment p
    where r.tourist_id=t.tourist_id
    and r.boat_id=b.boat_id
    and r.sailor_id=s.sailor_id
    and r.resv_id=p.resv_id
    and r.resv_id=R_rid;

    v_total := (v_adult+v_child)*v_price;

    if v_total>500 and v_total<2000 then
        v_discount := v_total*0.05;
    elsif v_total>=2000 and v_total<5000 then
        v_discount := v_total*0.10;
    elsif v_total>=5000 then
        v_discount := v_total*0.20;
    end if;

    v_final := v_total - v_discount;

    update payment
    set amount=v_final
    where resv_id=v_pid;

    if sql%found then
        dbms_output.put_line('tourist '||v_tname);
        dbms_output.put_line('boat '||v_bname||' type '||v_type);
        dbms_output.put_line('sailor '||v_sname);
        dbms_output.put_line('total amount '||v_total);
        dbms_output.put_line('discount '||v_discount);
        dbms_output.put_line('amount to be paid '||v_final);
    else
        dbms_output.put_line('payment update failed');
    end if;

exception
    when no_data_found then
        dbms_output.put_line('reservation or payment not found');
end;
/

exec generate_bill('R014');

rem 5. procedure that accepts tourist budget and preferred boat type and recommends most frequently reserved boat

create or replace procedure recommend_boat(p_budget in number, p_type in boat.type%type) is

    cursor c1 is
        select b.boat_name, b.price, count(r.resv_id) trip_count
        from boat b, reservation r
        where b.boat_id=r.boat_id
        and b.type=p_type
        group by b.boat_name, b.price
        order by trip_count desc;

    v_name boat.boat_name%type;
    v_price boat.price%type;
    v_count number;
    v_trips number;

begin
    open c1;
    fetch c1 into v_name, v_price, v_count;

    if c1%notfound then
        dbms_output.put_line('no boats of this type');
    else
        if v_price<=p_budget then
            v_trips := floor(p_budget/v_price);
            dbms_output.put_line('recommended boat '||v_name);
            dbms_output.put_line('trips you can afford '||v_trips);
        else
            dbms_output.put_line('no boat within budget');
        end if;
    end if;

    close c1;
end;
/


exec recommend_boat(5000,'LUX');



rem 6. function that returns tourist name who made highest number of reservations for a boat

create or replace function top_tourist(p_bid in reservation.boat_id%type)
return varchar2 is

    v_name tourist.tourist_name%type;

begin
    select t.tourist_name
    into v_name
    from reservation r, tourist t
    where r.tourist_id = t.tourist_id
    and r.boat_id = p_bid
    group by t.tourist_name
    having count(*) = (
        select max(cnt)
        from (
            select count(*) cnt
            from reservation
            where boat_id = p_bid
            group by tourist_id
        )
    );

    return v_name;

exception
    when no_data_found then
        return 'no bookings';
end;
/


declare
    v_name varchar2(20);
begin
    v_name := top_tourist('B001');
    dbms_output.put_line('top tourist '||v_name);
end;
/
