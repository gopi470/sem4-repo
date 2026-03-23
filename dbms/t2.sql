-- SELECT rpad(salary,5,'@'),lpad(salary,9,'@') from employees;

-- select sysdate-5 from employees;


-- select next_day(sysdate,'FRIDAY') from employees;



-- select to_char(sysdate,'dd month yyyy') from employees;

-- SELECT 
--     ROUND(AVG(salary)) AS avg,
--     MAX(salary)        AS max,
--     MIN(salary)        AS min,
--     SUM(salary)        AS sum
-- FROM employees;

SELECT MONTHS_BETWEEN(
       DATE '2026-02-10',
       DATE '2024-02-10')  AS years_diff
FROM dual;

SELECT * FROM dual;

SELECT (DATE '2026-02-10' - DATE '2026-01-10') / 7 AS weeks_diff
FROM dual;

SELECT NEXT_DAY(SYSDATE, 'MONDAY') FROM dual;


SELECT EXTRACT(YEAR FROM SYSDATE) FROM dual;
SELECT EXTRACT(MONTH FROM SYSDATE) FROM dual;
SELECT EXTRACT(DAY FROM SYSDATE) FROM dual;


SELECT TO_CHAR(SYSDATE, 'DD-MM-YYYY') FROM dual;
SELECT TO_CHAR(SYSDATE, 'DAY') FROM dual;

SELECT LAST_DAY(SYSDATE) FROM dual;
