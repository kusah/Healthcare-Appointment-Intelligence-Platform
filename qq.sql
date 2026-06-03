CREATE DATABASE healthcare_db;
USE healthcare_db;
select DATABASE();
SHOW tables;
USE healthcare_db;

CREATE TABLE appointments_raw (
    PatientId BIGINT,
    AppointmentID BIGINT PRIMARY KEY,
    Gender VARCHAR(10),
    ScheduledDay DATETIME,
    AppointmentDay DATETIME,
    Age INT,
    Neighbourhood VARCHAR(100),
    Scholarship TINYINT,
    Hipertension TINYINT,
    Diabetes TINYINT,
    Alcoholism TINYINT,
    Handcap TINYINT,
    SMS_received TINYINT,
    No_show VARCHAR(5)
);
SHOW tables;
DESCRIBE appointments_raw;
SELECT COUNT(*) FROM appointments_raw;
SELECT COUNT(*) AS total_records
FROM appointments_raw;
SELECT * 
FROM appointments_raw
LIMIT 5;
SELECT
ROUND(
100 * SUM(CASE WHEN No_show='Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS No_Show_Rate
FROM appointments_raw;
SELECT
Gender,
COUNT(*) AS total
FROM appointments_raw
GROUP BY Gender;
SELECT COUNT(DISTINCT PatientId) AS total_patients
FROM appointments_raw;
