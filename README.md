# Pharmacy Management System

## Technologies Used:
- **Python**
- **MSSQL**
- **PyODBC**

## Description:
The Pharmacy Management System is a command-line interface (CLI) tool that helps manage medication inventory, employee records, and sales transactions. The system provides features for user authentication, inventory management, sales tracking, and reporting. It is designed to streamline pharmacy operations by automating key tasks and providing real-time insights.

## Key Features & Responsibilities:

- ✅ **Database Management**: Designed and implemented a Microsoft SQL Server (MSSQL) database with efficient indexing and relationships for managing employees, medicines, and sales.
  
- ✅ **CRUD Operations**: Developed features for creating, reading, updating, and deleting records related to medicines, employees, and sales transactions.

- ✅ **User Authentication**: Implemented a simple login system with user roles (Owner, Manager, Receptionist) for access control (currently working on adding password hashing for added security).

- ✅ **Stock & Low Stock Alerts**: Automated inventory management, including real-time stock updates and alerts for low stock levels on medicines.

- ✅ **Sales Reporting**: Created SQL-based reports to generate monthly sales data, track employee performance, and identify top-selling medicines.

- ✅ **Triggers & Views**: Implemented triggers to automatically update medicine stock after each sale and views to calculate total sales.

- ✅ **Python-MSSQL Integration**: Used PyODBC to connect Python with MSSQL, enabling smooth database transactions and data retrieval.

---

## Roles and Permissions

### Owner

As an **Owner**, you have full control over the system and can perform the following actions:

1. **Add Employee**: You can add new employees with roles such as Manager or Receptionist.
2. **Change Role**: You can change the role of an employee between Manager and Receptionist.
3. **View All Employees**: You can view the list of all employees in the system.
4. **View All Medicines**: You can view the complete list of available medicines.
5. **Add Medicine**: You can add new medicines to the system.
6. **View All Patients**: You can view a list of all patients.
7. **Update Medicine**: You can update medicine details such as stock and price.
8. **Insert Record**: You can add sales or other relevant records.
9. **Low Stock Alert**: You receive alerts when any medicine is running low in stock.
10. **Sales Overview**: You can view the total sales and revenue from the last month.
11. **Employee Sales Performance**: You can see how well each employee is performing in terms of sales.
12. **Top Selling Medicines**: View a list of the top-selling medicines based on the quantity sold.
13. **Most Frequent Patients**: View the top 10 patients who purchase the most frequently.

### Manager

As a **Manager**, you have the following permissions:

1. **View All Medicines**: You can view the complete list of available medicines.
2. **View All Patients**: You can view a list of all patients.
3. **Add Medicine**: You can add new medicines to the system.
4. **Update Medicine**: You can update medicine details such as stock and price.
5. **Insert Record**: You can add sales or other relevant records.
6. **Low Stock Alert**: You will receive alerts when any medicine is running low in stock.

### Receptionist

As a **Receptionist**, your permissions are more limited:

1. **Insert Record**: You can add sales or other relevant records.
2. **View All Patients**: You can view the list of all patients in the system.

## Installation

1. Clone this repository to your local machine.
2. Start SQL Server in SQL Server Management Studio (SSMS).
3. Create the necessary tables by running the `\database.sql` script.
4. Populate the tables with initial data by running the `\database\data.sql` script.
5. Run the application by executing `main.py` in the root directory using the following command:
   ```bash
   python main.py

