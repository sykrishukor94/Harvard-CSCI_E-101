SELECT * FROM nj_teachers.nj_teachers_salaries;
select count(primary_job) FROM nj_teachers.nj_teachers_salaries;
SELECT last_name, first_name, max(salary) FROM nj_teachers.nj_teachers_salaries WHERE primary_job ='Preschool' GROUP BY last_name, first_name, salary order by salary DESC;
SELECT salary FROM nj_teachers.nj_teachers_salaries WHERE last_name= 'Smith' AND first_name='Brittany M';
SELECT last_name, first_name, salary FROM nj_teachers.nj_teachers_salaries WHERE primary_job = 'Preschool' order by salary DESC;
SELECT COUNT(primary_job='Preschool') FROM nj_teachers.nj_teachers_salaries WHERE district='Passaic City';
SELECT AVG(experience_total) FROM nj_teachers.nj_teachers_salaries WHERE district='Passaic City' AND primary_job = 'Preschool';
SELECT experience_total FROM nj_teachers2.nj_teachers_salaries WHERE primary_job = 'Preschool' order by experience_total+0 DESC;
