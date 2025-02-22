create database PharmacyDB;

use PharmacyDB;

-- Employee Table
create table employee(
Emp_ID int primary key identity(1,1),
First_Name varchar(20) not null,
Last_Name varchar(20) not null,
Username varchar(20) not null,
Pass varchar(20) not null,
Designation varchar(20) check (Designation in ('Owner','Manager','Receptionist')),
Login_Role varchar(20) check (Login_Role in ('admin','manager', 'user'))
);

-- Medicines Table
create table medicines(
Med_ID int primary key identity(1,1),
Med_name varchar(20) not null,
Category varchar(20) not null,
Stock int not null,
Buying_Price int not null,
Selling_Price int not null,
Exp_Date date not null
);

-- Patient Table
create table patient(
Patient_ID int primary key identity(1,1),
First_Name varchar(20) not null,
Last_Name varchar(20) not null,
Mobile_No bigint not null
);

-- Sales Table
create table sales(
sales_id int primary key identity(1000,1),
Emp_ID int foreign key references employee(Emp_ID),
Patient_ID int foreign key references patient(Patient_ID),
Med_ID int foreign key references medicines(Med_ID),
Quantity int not null,
Order_Date datetime default GETDATE(),
Payment_Method varchar(10) CHECK (Payment_Method IN ('Cash', 'Card'))
);