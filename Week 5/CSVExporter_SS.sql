# From week 5 - practice set
-- SELECT * FROM cookies.sales;
-- SELECT 'Temperature', 'Sales' from cookies.sales - possible not pretty probel; FROM cookie.sales is unnecessary
SELECT 'Temperature', 'Sales'
UNION
(SELECT DISTINCT Temperature, Sales FROM cookies.sales
ORDER BY RAND(7)
LIMIT 25)
# From Google
-- SELECT DISTINCT Temperature, Sales FROM cookies.sales WHERE Sales >= RAND(7) * 
--     ( SELECT MAX(Sales) FROM cookies.sales) 
-- ORDER BY Sales LIMIT 100

INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/test100.csv'
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
