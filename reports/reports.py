from libs.connection import connect_db
import pandas as pd

def low_stock():
    conn=connect_db()
    if conn:
        query = "SELECT Med_ID,Med_name,Stock FROM medicines WHERE Stock < 50"
        lowstock = pd.read_sql(query, conn)
        conn.close()
        return lowstock
    else:
        print("Error fetching medicines stock")
        return None

def emp_perf():
    conn=connect_db()
    if conn:
        query = '''SELECT 
    e.First_Name, 
    e.Last_Name, 
    COUNT(s.Med_ID) AS Total_Sales,
    SUM(s.Quantity * m.Selling_Price) AS Total_Revenue
FROM sales s
JOIN employee e ON s.Emp_ID = e.Emp_ID
JOIN medicines m ON s.Med_ID = m.Med_ID
GROUP BY e.Emp_ID,e.First_Name, 
    e.Last_Name
ORDER BY Total_Revenue DESC'''
        perf = pd.read_sql(query, conn)
        conn.close()
        return perf
    else:
        print("Error fetching employee performance")
        return None


def top_med():
    conn=connect_db()
    if conn:
        query = '''SELECT top 3
    m.Med_name, 
    SUM(s.Quantity) AS Total_Quantity_Sold,
    SUM(s.Quantity * m.Selling_Price) AS Total_Revenue
FROM sales s
JOIN medicines m ON s.Med_ID = m.Med_ID
GROUP BY m.Med_name
ORDER BY Total_Quantity_Sold DESC;'''
        topmed = pd.read_sql(query, conn)
        conn.close()
        return topmed
    else:
        print("Error fetching sales data")
        return None

def freq_patient():
    conn=connect_db()
    if conn:
        query = '''SELECT top 2
    p.First_Name, 
    p.Last_Name, 
    COUNT(s.Patient_ID) AS Purchase_Frequency,
    SUM(s.Quantity * m.Selling_Price) AS Total_Spent
FROM sales s
JOIN patient p ON s.Patient_ID = p.Patient_ID
JOIN medicines m ON s.Med_ID = m.Med_ID
GROUP BY p.Patient_ID,p.First_Name, 
    p.Last_Name
ORDER BY Purchase_Frequency DESC;'''
        pat_freq = pd.read_sql(query, conn)
        conn.close()
        return pat_freq
    else:
        print("Error fetching sales data")
        return None

def sales_overview():
    conn=connect_db()
    if conn:
        query = '''SELECT 
    MONTH(s.Order_Date) AS Month,
    YEAR(s.Order_Date) AS Year,
    SUM(s.Quantity * m.Selling_Price) AS Total_Revenue
FROM sales s
JOIN medicines m ON s.Med_ID = m.Med_ID
WHERE s.Order_Date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY YEAR(s.Order_Date), MONTH(s.Order_Date)
ORDER BY YEAR(s.Order_Date) DESC, MONTH(s.Order_Date) DESC;'''
        sale = pd.read_sql(query, conn)
        conn.close()
        return sale
    else:
        print("Error fetching sales data")
        return None