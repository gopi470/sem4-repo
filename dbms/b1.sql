drop table Product;


rem:create table
create table Product(
  pid varchar(10) CONSTRAINT pk_pid primary key,
  food varchar2(20),
  flavor varchar2(20),
  price NUMBER(4,2));


rem:Insert first row (no column names) 
INSERT INTO Product
VALUES ('20-BC-C-10','Chocolate','Cake',8.95);
SELECT * FROM Product;


rem:Q2: Insert second & third rows with column names

INSERT INTO Product (pid, food, flavor, price)
VALUES ('20-BC-L-10','Lemon','Cake',8.95);

INSERT INTO Product (food,pid, flavor, price)
VALUES ('Casino','20-CA-7.5','Cake',15.95);
SELECT * FROM Product;



rem:Q3: Display populated tuples
SELECT * FROM Product;

rem:Q4: INSERT statement in a text file named loadproduct.sql to load seven rows
rem:add rows using loadproduct.sql
@ Z:\dbms\loadproduct.sql
SELECT * FROM Product;


rem:Q5: Populate the table with the next seven rows 
@ Z:\dbms\loadproduct3.txt
SELECT * FROM Product;

rem: Q6: Update price of specific product
UPDATE Product
SET price = 32.00
WHERE pid = '24-8x10';

rem:Display 
SELECT * FROM Product;

rem: Q7: Increase price by 10%
UPDATE Product
SET price = price * 1.10
WHERE flavor = 'Eclair' AND food LIKE 'C%';

SELECT * FROM Product;


rem:Q8: Delete all Blueberry food items
DELETE FROM Product WHERE food = 'Blueberry';

rem:Q9: Confirm changes 
SELECT * FROM Product;

rem: Q10: Commit changes 
COMMIT;

rem: Q11: Insert last row from loadproduct.sql
@ Z:\dbms\loadproduct2.txt


rem: Q12: Confirm insertion 
SELECT * FROM Product;

rem: Q13: Discard recently populated row 
ROLLBACK;

rem: Q14: Repeat confirmation 
rem:add rows using loadproduct.txt
@ Z:\dbms\loadproduct2.txt
SELECT * FROM Product;

rem: Q15: Mark intermediate point 
SAVEPOINT sp1;

rem: Q16: Empty entire PRODUCT table 
DELETE FROM Product;

SELECT * FROM Product;


rem: Q17: Confirm table is empty 
SELECT * FROM Product;

rem: Q18: Discard most recent DELETE 
ROLLBACK to sp1;


rem: Q19: Confirm data is intact 
SELECT * FROM Product;

rem: Q20: Make data addition permanent 
COMMIT;

rem: Q21: price = 3.25 OR (food='Apple' AND flavor='Tart') 
SELECT *
FROM Product
WHERE price = 3.25 OR (food = 'Apple' AND flavor = 'Tart');

rem: Q22: Select when Price = 3.25 AND food contains 'e' 
SELECT *
FROM Product
WHERE price = 3.25 AND food LIKE '%e%';

rem: Q23: Food starts with V, N, or T 
SELECT *
FROM Product
WHERE (food like 'V%' 
or food like 'N%' 
or food like 'T%');

rem: Q24: Unique flavours 
SELECT DISTINCT flavor
FROM Product;

rem: Q25: Display product info in ascending order of price 
SELECT *
FROM Product
ORDER BY price;

rem: Q26: Add expiry date & update to sysdate + 5 

ALTER TABLE Product
ADD expiry_date DATE;

UPDATE Product
SET expiry_date = SYSDATE + 5;

SELECT * FROM Product;



