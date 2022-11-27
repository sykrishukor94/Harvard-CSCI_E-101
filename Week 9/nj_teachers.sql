# CSCI E-101 Week 5
# Managing Data Exercise 2
# Syukri Shukor

# Selecting 777 random records with seed(7) 
SELECT 'last_name', 'first_name', 'county', 'district', 'school', 'primary_job', 'fte', 'salary', 'certificate', 'subcategory', 'teaching_route', 'highly_qualified', 'experience_district', 'experience_nj', 'experience_total'
UNION
(SELECT DISTINCT * FROM nj_state_teachers_salaries.nj_state_teachers_salaries # Include all columns
ORDER BY RAND(7)
LIMIT 777)

# Export random samples to another .csv
-- INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/teachersample.csv'
INTO OUTFILE '/autograder/submission/teachersample.csv'
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';

# Create a new database
CREATE SCHEMA teacher_sample;

# Create a new table
CREATE TABLE teacher_sample.teachers
 (last_name TEXT, 
 first_name TEXT,
 county TEXT,
 district TEXT,
 school TEXT,
 primary_job TEXT,
 fte FLOAT NOT NULL,
 salary INT NOT NULL,
 certificate TEXT,
 subcategory TEXT,
 teaching_route TEXT,
 highly_qualified TEXT,
 experience_district INT NOT NULL,
 experience_nj INT NOT NULL,
 experience_total INT NOT NULL);

# Populate new table with teachersample.csv
-- LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/teachersample.csv' INTO TABLE teacher_sample.teachers FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
LOAD DATA INFILE '/autograder/source/teachersample2.csv' INTO TABLE teacher_sample.teachers FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;


# Calculations
#	Calculate the average salary
SELECT AVG(salary) FROM teacher_sample.teachers;

#	Calculate the number of people whose salary is more than 150,000
SELECT count(salary) FROM teacher_sample.teachers WHERE salary > 150000;

#	Get the last name of the ones who make more than 150,000 but has less than 5 years of total experience
SELECT last_name FROM teacher_sample.teachers WHERE salary > 150000 AND experience_total < 5;

#	Get the highest salary for Preschool, School Counselor, Principal (anyone with the word Principal in the title) , School Psychologist, and Kindergart 
#		('Preschool',
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job = 'Preschool';
#		'School Counselor',
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job = 'School Counselor';
#		contains('Principal'),
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job LIKE '%Principal%';
#		'School Psychologist',
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job = 'School Psychologist';
#		'Kindergarten')
SELECT MAX(salary) FROM teacher_sample.teachers WHERE primary_job = 'Kindergarten';

#	'last_name','first_name','salary' of MIN('salary') in 'Atlantic City'
SELECT last_name, first_name, salary FROM teacher_sample.teachers WHERE district = 'Atlantic City' AND salary = (SELECT MIN(salary) FROM teacher_sample.teachers WHERE district = 'Atlantic City');

# Total row of employees in 'Passaic City' with 'experience_total' >10
SELECT count(first_name) FROM teacher_sample.teachers WHERE district = 'Passaic City' AND experience_total > 10;