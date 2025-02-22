from libs.connection import connect_db
import pandas as pd

def medicines_table():
    conn = connect_db()
    if conn:
        query = "Select * from medicines"
        med = pd.read_sql(query, conn)
        conn.close()
        return med
    else:
        print("Error fetching Inventory Data.")
        return None

def add_medicines():
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    medname = input("Enter the name of Medicine: ")
    cat = input("Enter Category: ")
    stock = int(input("Enter Stock: "))
    buy = int(input("Enter Buying Price: "))
    sell = int(input("Enter Selling Price : "))
    exp = input("Enter Expiry date in 'YYYY-MM-DD': ")
    
    try:
        cursor.execute("INSERT INTO medicines (Med_name, Category, Stock, Buying_Price, Selling_Price, Exp_Date) VALUES (?, ?, ?, ?, ?, ?)", 
                       (medname, cat, stock, buy, sell, exp))
        conn.commit()
        print("Medicine added in Inventory.")
    except Exception as e:
        print("Error adding medicine:", e)
    finally:
        conn.close()

def med_update():
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    medname = input("Enter the name of Medicine to be updated: ")
    stock = int(input("Enter the updated Stock: "))
    exp = input("Enter Expiry date in 'YYYY-MM-DD': ")

    try:
        cursor.execute("UPDATE medicines SET Stock = ?, Exp_Date = ? WHERE Med_name = ?",(stock,exp,medname))
        conn.commit()
        print("Inventory updated successfully.")
    except Exception as e:
        print("Error in modifying inventory:", e)
    finally:
        conn.close()