# From Week 5 - practice
-- DROP TABLE nj_state_teachers_salaries;
DROP SCHEMA nj_state_teachers_salaries;
-- CREATE SCHEMA cookies;
-- CREATE TABLE nj_state_teachers_salaries.nj_state_teachers_salaries
--  (last_name TEXT, 
--  first_name TEXT,
--  county TEXT,
--  district TEXT,
--  school TEXT,
--  primary_job TEXT,
--  fte FLOAT NOT NULL,
--  salary INT NOT NULL,
--  certificate TEXT,
--  subcategory TEXT,
--  teaching_route TEXT,
--  highly_qualified TEXT,
--  experience_district INT NOT NULL,
--  experience_nj INT NOT NULL,
--  experience_total INT NOT NULL);
-- LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/nj_state_teachers_salaries_cleaned.csv' INTO TABLE nj_state_teachers_salaries.nj_state_teachers_salaries FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 ROWS