-- DROP DATABASE student_management;
CREATE DATABASE student_management;
use student_management;
CREATE TABLE stud_details (
	id int not null auto_increment primary key,
    stud_name varchar(120),
    address varchar(120),
    course varchar(120),
    active_stautus Boolean DEFAULT TRUE,
    created_at timestamp default current_timestamp
);
-- drop table stud_details;
select * from stud_det;
show warnings;
show Errors;
insert into  stud_details (id,stud_name,address,course) values(12,"Suresh","Trichy","python");
insert into  stud_details (stud_name,address,course) values("surya","Chennai","python"),('Ganesh',"Chennai","python"),('Naveen','Madurai','java');
-- update stud_details set stud_name="Ram" where id=10;
-- update stud_details set stud_name="Sam",course="java" where id=9 and stud_name="Ganesh";
-- delete from stud_details where id=12;

-- task  1. Create Employee_management database  2. create employee table emp_name,department, salary,active_status,created_at

-- Syntax: ALTER TABLE old_tablename RENAME TO new_tablename;
alter table stud_details rename to stud_det;
-- SYNTAX : ALTER TABLE table_name RENAME COLUMN old_column_name to NEW_column_name
alter table stud_det rename column active_stautus to active_status;
-- SYNTAX :  ALTER TABLE table_name ADD COLUMN col_name Data_type constraints AFTER column_name;
ALTER TABLE stud_det ADD COLUMN mobile_no varchar(20)  AFTER address;
ALTER TABLE stud_det ADD COLUMN email_id int  not null AFTER mobile_no;
-- SYNTAX ALTER TABLE table_name MODIFY COLUMN column_name new_data_type [contraints];
alter table stud_det modify column mobile_no varchar(30) ;
alter table stud_det modify column email_id varchar(30) null;
describe stud_det;
-- Filters
select stud_name,course from stud_det;
select stud_name,course from stud_det where course ="python";
-- update stud_det set email_id="sanjeev@gmail.com" where id=2;
select * from stud_det where stud_name="Deepak" and course="php";
select * from stud_det where course in("java","php");
select * from stud_det where course not in("java","php");
-- update stud_det set stud_name="raja",address="salem",email_id="raja@gmail.com" where id=19;
select * from stud_det where email_id like "%raja%";
select * from stud_det where email_id like "raja%";
select * from stud_det where email_id like "%@gmail.com";
select * from stud_det where email_id like "____@gmail.com";
select course, count(*) as student_count  from stud_det group by course having student_count<=5;
select * from stud_det where course="python";
select * from stud_det order by course ;
select * from stud_det order by course desc; -- ASC
select * from stud_det  limit 4,10;



