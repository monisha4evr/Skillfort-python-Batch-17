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
select * from stud_details;
show warnings;
insert into  stud_details (stud_name,address,course) values("Suresh","Trichy","python");
insert into  stud_details (stud_name,address,course) values("surya","Chennai","python"),('Ganesh',"Chennai","python"),('Naveen','Madurai','java');
-- update stud_details set stud_name="Ram" where id=10;
-- update stud_details set stud_name="Sam",course="java" where id=9 and stud_name="Ganesh";
-- delete from stud_details where id=12;

-- task  1. Create Employee_management database  2. create employee table emp_name,department, salary,active_status,created_at

