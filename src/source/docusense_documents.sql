use docusense;
create table Docusense_document_type(Project_id int , document_type_code varchar(15),document_type_name varchar(15));
insert into Docusense_document_type(Project_id,document_type_code,document_type_name) values(1,'OFC_INV','Office Invoice'),(2,'BK_ST','Bank statement'),
(3,'MD_RE','Medical Receipt'),(4,'SL_SP','Sallery slip'),(5,'GR_RE','Grocery_receipt');
select * from docusense_document_type; 

create table Docusense_document_Database(Project_id int , document_type_code varchar(15),document_type_name varchar(15),doc_create_date Date,Doc_Status varchar(15),Reviewer_ID varchar(15),Last_modified_date Date);
insert into Docusense_document_Database(Project_id, document_type_code, document_type_name, doc_create_date,Doc_Status, Reviewer_ID, Last_modified_date)
values(1,'OFC_INV','Office Invoice',STR_TO_DATE('12/01/2022', '%d/%m/%Y'),'Uploaded','RT_01',STR_TO_DATE('22/06/2022', '%d/%m/%Y')),
(2,'BK_ST','Bank statement',STR_TO_DATE('23/03/2022', '%d/%m/%Y'),'Extracted','RT_02',STR_TO_DATE('28/07/2022', '%d/%m/%Y')),
(3,'MD_RE','Medical Receipt',STR_TO_DATE('25/03/2022', '%d/%m/%Y'),'In review','RT_03',STR_TO_DATE('29/07/2022', '%d/%m/%Y')),
(4,'SL_SP','Sallery slip',STR_TO_DATE('27/04/2022', '%d/%m/%Y'),'Saved','RT_01',STR_TO_DATE('02/08/2022', '%d/%m/%Y')),
(5,'GR_RE','Grocery_receipt',STR_TO_DATE('25/05/2022', '%d/%m/%Y'),'Submitted','RT_01',STR_TO_DATE('14/08/2022', '%d/%m/%Y'));

select * from Docusense_document_Database;