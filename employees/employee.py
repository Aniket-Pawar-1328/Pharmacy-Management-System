from libs.connection import connect_db
import pandas as pd

def employee_table():
    conn = connect_db()
    if conn:
        query = "SELECT * FROM employee"
        emp = pd.read_sql(query, conn)
        conn.close()
        return emp
    else:
        print("Error fetching employee data.")
        return None

def add_employee():
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    firstname = input("Enter First Name of Employee: ")
    lastname = input("Enter Last Name of Employee: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    designation = input("Choose Role: 1. Manager\n2. Receptionist: ")
    
    if designation == "1":
        designation = "Manager"
        role = "manager"
    elif designation == "2":
        designation = "Receptionist"
        role = "user"
    else:
        print("Invalid role selected. Please choose 1 for Manager or 2 for Receptionist.")
        return

    try:
        cursor.execute("INSERT INTO employee (First_Name, Last_Name, Username, Pass, Designation, Login_Role) VALUES (?, ?, ?, ?, ?, ?)", 
                       (firstname, lastname, username, password, designation, role))
        conn.commit()
        print("Employee added successfully.")
    except Exception as e:
        print("Error adding employee:", e)
    finally:
        conn.close()


def employee_update():
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    username = input("Enter username whose role to be changed: ")
    designation = input("Choose Role to be assigned: 1. Owner\n2. Manager\n3. Receptionist:\n ")
    
    if designation == "1":
        designation = "Owner"
        role = "admin"
    elif designation == "2":
        designation = "Manager"
        role = "manager"
    elif designation == "3":
        designation = "Receptionist"
        role = "user"
    else:
        print("Invalid role selected. Please choose 1 for Owner, 2 for Manager or 3 for Receptionist.")
        return
    try:
        cursor.execute("UPDATE employee SET Designation = ?, Login_Role = ? WHERE Username = ?",(designation,role,username))
        conn.commit()
        print("Employee Details Modified successfully.")
    except Exception as e:
        print("Error Modified Employee Details:", e)
    finally:
        conn.close()