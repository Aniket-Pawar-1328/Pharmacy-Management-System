from libs.connection import connect_db
import pandas as pd

def patient_table():
    conn = connect_db()
    if conn:
        query = "Select * from patient"
        pat = pd.read_sql(query, conn)
        conn.close()
        return pat
    else:
        print("Error fetching Patient's data.")
        return None