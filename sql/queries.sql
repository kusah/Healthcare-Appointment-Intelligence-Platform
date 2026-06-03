-- =====================================================
-- Healthcare Appointment Intelligence Platform
-- Analytics Queries
-- =====================================================

-- 1. Total Records
SELECT COUNT(*) AS total_records
FROM appointments_raw;

-- 2. No Show Rate
SELECT
ROUND(
100 * SUM(CASE WHEN No_show='Yes' THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS No_Show_Rate
FROM appointments_raw;

-- 3. Total Unique Patients
SELECT COUNT(DISTINCT PatientId)
AS Total_Patients
FROM appointments_raw;

-- 4. Gender Distribution
SELECT
Gender,
COUNT(*) AS Total
FROM appointments_raw
GROUP BY Gender;

-- 5. Top 10 Neighbourhoods
SELECT
Neighbourhood,
COUNT(*) AS Total_Appointments
FROM appointments_raw
GROUP BY Neighbourhood
ORDER BY Total_Appointments DESC
LIMIT 10;

-- 6. Average Age
SELECT
ROUND(AVG(Age),2) AS Average_Age
FROM appointments_raw;

-- 7. Diabetes Distribution
SELECT
Diabetes,
COUNT(*) AS Total
FROM appointments_raw
GROUP BY Diabetes;

-- 8. Hypertension Distribution
SELECT
Hipertension,
COUNT(*) AS Total
FROM appointments_raw
GROUP BY Hipertension;

-- 9. SMS Received Distribution
SELECT
SMS_received,
COUNT(*) AS Total
FROM appointments_raw
GROUP BY SMS_received;

--10. Missing values
SELECT
SUM(CASE WHEN PatientId IS NULL THEN 1 ELSE 0 END) AS Missing_PatientId,
SUM(CASE WHEN Gender IS NULL THEN 1 ELSE 0 END) AS Missing_Gender,
SUM(CASE WHEN Age IS NULL THEN 1 ELSE 0 END) AS Missing_Age
FROM appointments_raw;

--11. Age Issues 
SELECT
MIN(Age) AS Min_Age,
MAX(Age) AS Max_Age,
AVG(Age) AS Avg_Age
FROM appointments_raw;
--Got error because of negative age values, so we will filter those out in the next query
SELECT *
FROM appointments_raw
WHERE Age < 0 OR Age > 100;
-- created a view
CREATE VIEW appointments_clean AS
SELECT *
FROM appointments_raw
WHERE Age BETWEEN 0 AND 100;
-- affected record
SELECT COUNT(*) AS Outlier_Records
FROM appointments_raw
WHERE Age < 0 OR Age > 100;

SELECT
ROUND(
100 * COUNT(*) /
(SELECT COUNT(*) FROM appointments_raw),
4
) AS Outlier_Percentage
FROM appointments_raw
WHERE Age < 0 OR Age > 100;


--12. Avg Age
SELECT
ROUND(AVG(Age),2) AS Average_Age
FROM appointments_raw;

--13. SMS Effectiveness Analysis
SELECT
SMS_received,
COUNT(*) AS Total_Appointments,
SUM(CASE WHEN No_show='Yes' THEN 1 ELSE 0 END) AS No_Shows,
ROUND(
100 * SUM(CASE WHEN No_show='Yes' THEN 1 ELSE 0 END) / COUNT(*),
2
) AS No_Show_Rate
FROM appointments_raw
GROUP BY SMS_received;

--14. Diabetes vs No-Show
SELECT
Diabetes,
COUNT(*) AS Total_Appointments,
SUM(CASE WHEN No_show='Yes' THEN 1 ELSE 0 END) AS No_Shows
FROM appointments_raw
GROUP BY Diabetes;

--15. Hypertension vs No-Show
SELECT
Hipertension,
COUNT(*) AS Total_Appointments,
SUM(CASE WHEN No_show='Yes' THEN 1 ELSE 0 END) AS No_Shows
FROM appointments_raw
GROUP BY Hipertension;

--16.Top 10 Neighbourhoods
SELECT
Neighbourhood,
COUNT(*) AS Total_Appointments
FROM appointments_raw
GROUP BY Neighbourhood
ORDER BY Total_Appointments DESC
LIMIT 10;

--17. 