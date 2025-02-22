from libs.connection import connect_db
import pandas as pd

def sales_table():
    conn = connect_db()
    if conn:
        query = "Select * from sales"
        sales = pd.read_sql(query, conn)
        conn.close()
        return sales
    else:
        print("Error fetching Sales data.")
        return None

def add_record():
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    emp = int(input("Enter Employee_ID: "))
    pat = int(input("Enter Patient_ID: "))
    med = int(input("Enter Medicine_ID: "))
    qty = int(input("Enter Quantity: "))
    od = input("Enter Order Date : ")
    pay = input("Choose Payment Method: 1. Cash\n2. Card: ")
    
    if pay == "1":
        pay = "Cash"
    elif pay == "2":
        pay = "Card"
    else:
        print("Invalid selectection. Please choose 1. Cash\n2. Card. \n")
        return
    
    try:
        cursor.execute("INSERT INTO sales (Emp_ID, Patient_ID, Med_ID, Quantity, Order_Date, Payment_Method) VALUES (?, ?, ?, ?, ?, ?)", 
                       (emp, pat, med, qty, od, pay))
        conn.commit()
        print("Sale Record added!")
    except Exception as e:
        print("Error adding sales record:", e)
    finally:
        conn.close()

