@ Z:\dbms\z1.sql;




set echo on;
set serveroutput on;

rem 1.check whether a boat of a given type and colour is available.


create or replace procedure boat_with_type_and_colour(
    p_type  in varchar2,
    p_color in varchar2
) is
begin
    for rec in (
        select boat_id, boat_name, capacity, price
        from boat
        where type = p_type
        and color = p_color
    )loop
        dbms_output.put_line('Boat ID: ' || rec.boat_id);
        dbms_output.put_line('Boat Name: ' || rec.boat_name);
        dbms_output.put_line('Capacity: ' || rec.capacity);
        dbms_output.put_line('Price: ' || rec.price);
    end loop;

    if sql%rowcount = 0 then
        dbms_output.put_line('No boat available of given type and color.');
    end if;
end;
/

begin
    boat_with_type_and_colour('CRU','Red');
end;
/




rem 2.find number of people who sailed on a given date.


create or replace procedure people_sailed(
    p_date in date
) is
    v_total number;
begin
    select sum(no_of_people)
    into v_total
    from reservation
    where sail_date = p_date;

    if v_total is null then
        dbms_output.put_line('No data available for given date.');
    else
        dbms_output.put_line('Total people sailed: ' || v_total);
    end if;

exception
    when no_data_found then
        dbms_output.put_line('No reservations found .');
end;
/

begin
    people_sailed('22-JAN-2005');
end;
/




rem 3.write a pl/sql procedure that takes a reservation id as input and, using an appropriate cursor and displays the details 
 

create or replace procedure reservation_details(
    p_resv_id in varchar2
) is
    cursor c1 is
        select t.tourist_name,
               b.boat_name,
               b.type,
               s.sailor_name,
               r.no_of_people,
               r.no_of_children
        from reservation r
        join tourist t on r.tourist_id = t.tourist_id
        join boat b on r.boat_id = b.boat_id
        join sailor s on r.sailor_id = s.sailor_id
        where r.resv_id = p_resv_id;

    rec c1%rowtype;
    v_total number;
begin
    open c1;
    fetch c1 into rec;

    if c1%notfound then
        dbms_output.put_line('Reservation not found.');
    else
        v_total := rec.no_of_people;

        dbms_output.put_line('Tourist: ' || rec.tourist_name);
        dbms_output.put_line('Boat: ' || rec.boat_name || ' (' || rec.type || ')');
        dbms_output.put_line('Sailor: ' || rec.sailor_name);
        dbms_output.put_line('Adults: ' || (rec.no_of_people - rec.no_of_children));
        dbms_output.put_line('Children: ' || rec.no_of_children);
        dbms_output.put_line('Total Passengers: ' || v_total);
    end if;

    close c1;
end;
/

begin
    reservation_details('R002');   
end;
/




rem 4.write a pl/sql procedure that accepts a reservation number and generates a bill with given discount

create or replace procedure generate_bill(
    p_resv_id in varchar2
) is

    v_tourist_name   tourist.tourist_name%type;
    v_boat_name      boat.boat_name%type;
    v_boat_type      boat.type%type;
    v_sailor_name    sailor.sailor_name%type;
    v_sail_date      reservation.sail_date%type;
    v_no_people      reservation.no_of_people%type;
    v_no_children    reservation.no_of_children%type;
    v_boat_price     boat.price%type;
    v_payment_id     payment.p_id%type;

    v_amount         number;
    v_discount       number := 0;
    v_discount_amt   number;
    v_final          number;

begin

    select t.tourist_name, b.boat_name,b.type,s.sailor_name,
           r.sail_date,r.no_of_people,r.no_of_children,b.price, p.p_id

    into   v_tourist_name,v_boat_name,v_boat_type,v_sailor_name,
           v_sail_date,v_no_people,v_no_children,v_boat_price,v_payment_id
    from reservation r
    join tourist t on r.tourist_id = t.tourist_id
    join boat b on r.boat_id = b.boat_id
    join sailor s on r.sailor_id = s.sailor_id
    join payment p on r.resv_id = p.resv_id
    where r.resv_id = p_resv_id;

    v_amount := v_boat_price * v_no_people;

    if v_amount > 500 and v_amount < 2000 then
        v_discount := 0.05;
    elsif v_amount >= 2000 and v_amount < 5000 then
        v_discount := 0.10;
    elsif v_amount >= 5000 then
        v_discount := 0.20;
    end if;

    v_discount_amt := v_amount * v_discount;
    v_final := v_amount - v_discount_amt;

    update payment
    set amount = v_final
    where p_id = v_payment_id;

    dbms_output.put_line('reservation number: ' || p_resv_id);
    dbms_output.put_line('tourist name: ' || v_tourist_name);
    dbms_output.put_line('sail date: ' || to_char(v_sail_date,'dd-mon-yyyy'));
    dbms_output.put_line('boat name: ' || v_boat_name || '  boat type: ' || v_boat_type);
    dbms_output.put_line('sailor name: ' || v_sailor_name);
  
    dbms_output.put_line('total amount = $ ' || to_char(v_amount,'9999.00'));
    dbms_output.put_line('discount (' || to_char(v_discount*100,'90') || '%) = $ ' || to_char(v_discount_amt,'9999.00'));
    
    dbms_output.put_line('amount to be paid = $ ' || to_char(v_final,'9999.00'));

exception
    when no_data_found then
        dbms_output.put_line('error: reservation not found');
    when others then
        dbms_output.put_line('unexpected error: ');

end;
/

begin
    generate_bill('R002');   
end;
/



rem 5.write a pl/sql procedure that accepts a tourists budget and preferred boat type, 
rem identifies the most frequently reserved boat of that type, checks whether it fits within 
rem the budget, and displays the recommended boat along with how many trips the tourist 
rem can afford, showing an appropriate message if no suitable boat is found.
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




rem 6.write a pl/sql function that accepts a boat id as input and returns the name of the 
rem tourist who has made the highest number of reservations for that boat, returning an 
rem appropriate message if no bookings exist. 

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
