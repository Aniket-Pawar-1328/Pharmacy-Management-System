import pyodbc
import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=UserWarning, message="pandas only supports SQLAlchemy connectable")

def connect_db():
    try:
        server = 'localhost\\SQLEXPRESS'
        database = 'PharmacyDB'
        conn = pyodbc.connect(f'''DRIVER={{SQL Server}};SERVER={server};DATABASE={database};''')
        #print("Connection Succesful")
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None