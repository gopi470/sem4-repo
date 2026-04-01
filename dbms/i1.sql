

CREATE TABLE Student_Fees (
    sid NUMBER PRIMARY KEY,
    sname VARCHAR2(50),
    course VARCHAR2(50),
    admission_date DATE,
    tuition_fee NUMBER,
    lab_fee NUMBER,
    library_fee NUMBER,
    scholarship NUMBER,
    gross_fee NUMBER,
    total_deduction NUMBER,
    net_fee NUMBER
);


CREATE OR REPLACE PROCEDURE calculate_fees(p_sid NUMBER) AS
BEGIN
    UPDATE Student_Fees
    SET 
        lab_fee = tuition_fee * 0.08,
        library_fee = tuition_fee * 0.05,
        scholarship = tuition_fee * 0.10,
        gross_fee = tuition_fee + (tuition_fee * 0.08) + (tuition_fee * 0.05),
        total_deduction = tuition_fee * 0.10,
        net_fee = (tuition_fee + (tuition_fee * 0.08) + (tuition_fee * 0.05)) 
                  - (tuition_fee * 0.10)
    WHERE sid = p_sid;
END;
/



INSERT INTO Student_Fees(sid, sname, course, admission_date, tuition_fee)
VALUES (1, 'Gopi', 'CSE', SYSDATE, 10000);

EXEC calculate_fees(1);

SELECT * FROM Student_Fees;


Select * from Student_Fees;