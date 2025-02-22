from libs.connection import connect_db

def authenticate():
    conn = connect_db()
    if not conn:
        return None, None
    
    cursor = conn.cursor()
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    cursor.execute("SELECT Login_Role FROM employee WHERE Username = ? AND Pass = ?", (username, password))
    result = cursor.fetchone()
    
    if result:
        return username, result[0]
    else:
        print("Invalid credentials!")
        return None, None


def logout(username):
    print(f"User {username} has been logged out.")
    conn = connect_db()
    if conn:
        conn.close()
    return