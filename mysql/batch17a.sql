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
ALTER TABLE stud_details ADD COLUMN depart varchar(20)  AFTER address;
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
-- Find the very first student(s) who registered
-- Show each student alongside their department's total strength
-- Find the maximum number of students enrolled in any single course
-- Join
-- 1. inner join
-- 2. cross join
-- 3. left join 
-- 4. right join 

select s.stud_name,s.course,d.department_name from stud_det as s inner join department as d on s.department = d.id
where d.department_name="it";
select s.stud_name,s.course,d.department_name from stud_det as s left join department as d on s.department = d.id;
select s.stud_name,s.course,d.department_name from stud_det as s right join department as d on s.department = d.id;

select * from stud_det where created_at=(select max(created_at) from stud_det);
select * from stud_det order by created_at desc limit 1;
select s.stud_name,s.address,s.department from stud_det as s where  exists (select 1 from department as d where d.id=s.department);
select * from department;
select * from stud_det;

select Course,count(*) as cnt from stud_det where course="python";
select max(created_at) from stud_det ;
select min(created_at) from stud_det ;
-- describe stud_det;
select sum(active_status) from stud_det; -- count total number -- sum total amount

select stud_name,(select count(*) from stud_det as innr where  o.department =innr.department ) as t from stud_det as o;
select * from stud_det as s where  exists (select 1 from department as d where s.department=d.id and d.id=1);
SELECT stud_name, depart FROM stud_details WHERE id < all (SELECT id FROM stud_det WHERE department = 2);
create view stud_det_view as select * from stud_det;
select * from stud_det_view;

show index from stud_det;
create index idx_stud_name on stud_det(stud_name);
drop index idx_stud_name on stud_det;
alter table stud_details  add constraint fk_stud_depart foreign key (depart) references department(id) on delete cascade;
select * from students;
describe students;

create database lighthouse;
use lighthouse;
show tables;
select * from app_product;


select * from stud_det;
describe stud_det;
insert into stud_det (stud_name,address) values ("Siva","Chennai");

