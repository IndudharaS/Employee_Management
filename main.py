from employee import Employee
from employee_dao import EmployeeDAO


def main():
    dao = EmployeeDAO()

    while True:
        print("\n==== Employee Management System ====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee by ID")
        print("6. Search Employee by Name")
        print("7. Show Total Number of Employees")
        print("8. Show Average Salary")
        print("9. Filter by Department")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                emp_id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                department = input("Enter Department: ")
                salary = float(input("Enter Salary: "))
                employee = Employee(emp_id, name, department, salary)
                dao.add_employee(employee)
            except ValueError:
                print("❌ Invalid input. Please enter correct values.")

        elif choice == '2':
            dao.view_employees()

        elif choice == '3':
            try:
                emp_id = int(input("Enter Employee ID to update: "))
                name = input("Enter new name (leave blank to skip): ") or None
                department = input(
                    "Enter new department (leave blank to skip): ") or None
                salary_input = input(
                    "Enter new salary (leave blank to skip): ")
                salary = float(salary_input) if salary_input.strip() else None
                dao.update_employee(emp_id, name, department, salary)
            except ValueError:
                print("❌ Invalid input. Please enter correct values.")

        elif choice == '4':
            try:
                emp_id = int(input("Enter Employee ID to delete: "))
                dao.delete_employee(emp_id)
            except ValueError:
                print("❌ Invalid ID.")

        elif choice == '5':
            try:
                emp_id = int(input("Enter Employee ID to search: "))
                dao.search_employee_by_id(emp_id)
            except ValueError:
                print("❌ Invalid ID.")

        elif choice == '6':
            name = input("Enter Employee Name to search: ")
            dao.search_employee_by_name(name)

        elif choice == '7':
            dao.count_employees()

        elif choice == '8':
            dao.average_salary()

        elif choice == '9':
            dept = input("Enter Department Name to filter: ")
            dao.filter_by_department(dept)

        elif choice == '10':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
