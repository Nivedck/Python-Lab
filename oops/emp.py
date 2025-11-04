class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


# ==========================
# Main Program Starts Here
# ==========================
employees = []   # List to store Employee objects

while True:
    print("\n========= EMPLOYEE MANAGEMENT MENU =========")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Get Attribute Value (getattr)")
    print("4. Check Attribute Existence (hasattr)")
    print("5. Add/Modify Attribute (setattr)")
    print("6. Delete Attribute (delattr)")
    print("7. View Employee __dict__")
    print("8. Delete Employee Object")
    print("9. Exit")
    print("============================================")

    choice = input("Enter your choice (1-9): ")

    # 1️⃣ Add new employee
    if choice == '1':
        name = input("Enter employee name: ")
        salary = float(input("Enter employee salary: "))
        emp = Employee(name, salary)
        employees.append(emp)
        print(f"Employee '{name}' added successfully!")

    # 2️⃣ Display all employees
    elif choice == '2':
        if not employees:
            print("No employees to display.")
        else:
            print("\nEmployee List:")
            for i, emp in enumerate(employees, start=1):
                print(f"\nEmployee {i}:")
                emp.show()

    # 3️⃣ Get attribute value
    elif choice == '3':
        if not employees:
            print("No employees available.")
        else:
            index = int(input("Enter employee number (1, 2, ...): ")) - 1
            attr = input("Enter attribute name: ")
            emp = employees[index]
            if hasattr(emp, attr):
                print(f"{attr} = {getattr(emp, attr)}")
            else:
                print(f"Attribute '{attr}' does not exist.")

    # 4️⃣ Check attribute existence
    elif choice == '4':
        index = int(input("Enter employee number: ")) - 1
        attr = input("Enter attribute name: ")
        emp = employees[index]
        print(hasattr(emp, attr))

    # 5️⃣ Add or modify attribute
    elif choice == '5':
        index = int(input("Enter employee number: ")) - 1
        attr = input("Enter new attribute name: ")
        value = input("Enter its value: ")
        setattr(employees[index], attr, value)
        print(f"Attribute '{attr}' added/updated successfully.")

    # 6️⃣ Delete attribute
    elif choice == '6':
        index = int(input("Enter employee number: ")) - 1
        attr = input("Enter attribute name to delete: ")
        emp = employees[index]
        if hasattr(emp, attr):
            delattr(emp, attr)
            print(f"Attribute '{attr}' deleted successfully.")
        else:
            print("Attribute not found.")

    # 7️⃣ View __dict__ of an employee
    elif choice == '7':
        index = int(input("Enter employee number: ")) - 1
        emp = employees[index]
        print("Current attributes:", emp.__dict__)

    # 8️⃣ Delete employee object
    elif choice == '8':
        index = int(input("Enter employee number to delete: ")) - 1
        del employees[index]
        print("Employee deleted successfully.")

    # 9️⃣ Exit
    elif choice == '9':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
