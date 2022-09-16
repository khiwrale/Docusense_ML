create schema docusense_ml;
USE docusense_ml;
create table Empl(id int , Ename varchar(15), destignation varchar(15),location varchar(15));
insert into Empl(id, Ename, destignation, location) values(001,'Samantak Panda','CEO','London'),(002,'Manoj Akella','AI/ML Head','Hyderabad'),(003,'Sumeet Shah','AI/ML TL','Pune'),
(004,'Dinesh Jamdade','ML Fresher','Nanded'),(005,'Kailas Hiwrale','ML Fresher','Nanded');
select * from Empl;

create database Docusense;
use Docusense;
create table Employee(id int , Ename varchar(15), destignation varchar(15),location varchar(15));
insert into Employee(id, Ename, destignation, location) values(001,'Samantak Panda','CEO','London'),(002,'Manoj Akella','AI/ML Head','Hyderabad'),(003,'Sumeet Shah','AI/ML TL','Pune'),
(004,'Dinesh Jamdade','ML Fresher','Nanded'),(005,'Kailas Hiwrale','ML Fresher','Nanded');
select * from Employee;

create table Docutype(id int , doctype varchar(15));
insert into Docutype(id, doctype) values(001,'Office INVOICE'),(002,'Salary slip '),(003,'Pdf File'),
(004,'Medical Receipt'),(005,'Pdf file');
select * from Docutype;
truncate table Docutype;

create table TuteckEmployee(id int , Ename varchar(15), destignation varchar(15),location varchar(15), doctype varchar(15));

insert into TuteckEmployee(id, Ename, destignation, location, doctype) values(001,'Samantak Panda','CEO','London','Office INVOICE'),
(002,'Manoj Akella','AI/ML Head','Hyderabad','Salary slip'),(003,'Sumeet Shah','AI/ML TL','Pune','Pdf File'),
(004,'Dinesh Jamdade','ML Fresher','Nanded','Medical Receipt'),(005,'Kailas Hiwrale','ML Fresher','Nanded','Pdf file');

select * from TuteckEmployee;
truncate table TuteckEmployee;

Create table DOCUSENSE_Document_db(Project_id int, doc_typ_cd () , doc_id (), doc_name, doc_create_date, doc_status (uploaded, extracted,In review,saved,submitted), 
Reviewer Id (), Last_modified ;