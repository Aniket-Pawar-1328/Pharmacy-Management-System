from libs.connection import connect_db
from authentication.authentication import authenticate, logout
from employees.employee import employee_table, add_employee, employee_update
from patients.patients import patient_table
from medicines.medicines import medicines_table, add_medicines, med_update
from sales.sales import sales_table, add_record
from reports.reports import low_stock, emp_perf, top_med, freq_patient, sales_overview

def main():
    print("\n💊 Welcome to Pharmacy Management System 💊")
    
    username, role = authenticate()
    
    if not username:
        return

    while True:
        if role == "admin":
            print("1. Add Employee\n2. Change Role\n3. View Employees\n4. View Medicines\n5. Add Medicine\n6. View Patients\n7. Update Medicine\n8. Insert Record\n9. Low Stock Alert\n10. Sales Overview\n11. Employee Sales Performance\n12. Top Selling Medicines\n13. Most Frequent Patients\n14. Logout")
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)
            except ValueError:
                print("Invalid choice, please enter a number.")
                continue

            if choice == 1:
                add_employee()
            elif choice == 2:
                employee_update()
            elif choice == 3:
                emp = employee_table()
                if emp is not None:
                    print(emp)
            elif choice == 4:
                med = medicines_table()
                if med is not None:
                    print(med)
            elif choice == 5:
                add_medicines()
            elif choice == 6:
                pat = patient_table()
                if pat is not None:
                    print(pat)
            elif choice == 7:
                med_update()
            elif choice == 8:
                add_record()
            elif choice == 9:
                lowstock = low_stock()
                if lowstock is not None:
                    print(lowstock)
            elif choice == 10:
                sovw = sales_overview()
                if sovw is not None:
                    print(sovw)
            elif choice == 11:
                empperf = emp_perf()
                if empperf is not None:
                    print(empperf)
            elif choice == 12:
                tm = top_med()
                if tm is not None:
                    print(tm)
            elif choice == 13:
                fp = freq_patient()
                if fp is not None:
                    print(fp)
            elif choice == 14:
                logout(username)
                break 
            else:
                print("Invalid choice!")

        elif role == "manager":
            print("1. View Medicines\n2. View Patients\n3. Add Medicine\n4. Update Medicine\n5. Insert Record\n6. Low Stock Alert\n7. Logout")
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)  
            except ValueError:
                print("Invalid choice, please enter a number.")
                continue
    
            if choice == 1:
                med = medicines_table()
                if med is not None:
                    print(med)
            elif choice == 2:
                pat = patient_table()
                if pat is not None:
                    print(pat)
            elif choice == 3:
                add_medicines()
            elif choice == 4:
                med_update()
            elif choice == 5:
                add_record()
            elif choice == 6:
                lowstock = low_stock()
                if lowstock is not None:
                    print(lowstock)
            elif choice == 7:
                logout(username)
                break  
            else:
                print("Invalid choice!")
    
        elif role == "user":
            print("1. Insert Record\n2. View Patients\n3. Logout")
            choice = input("Enter your choice: ")
            try:
                choice = int(choice)  
            except ValueError:
                print("Invalid choice, please enter a number.")
                continue
    
            if choice == 1:
                add_record()
            elif choice == 2:
                pat = patient_table()
                if pat is not None:
                    print(pat)
            elif choice == 3:
                logout(username)
                break
            else:
                print("Invalid choice!")
        else:
            print("Invalid Role!")
            break
        print("-------------------------------------------------------------------")
        print(" ")

# Run the main program
if __name__ == "__main__":
    main()