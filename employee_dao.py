from db_config import get_connection
from employee import Employee
from tabulate import tabulate


class EmployeeDAO:
    def employee_exists(self, emp_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM employees WHERE id = %s", (emp_id,))
        result = cursor.fetchone()[0]
        conn.close()
        return result > 0

    def add_employee(self, employee):
        if self.employee_exists(employee.emp_id):
            print("❌ Employee ID already exists. Try with a different ID.")
            return

        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO employees (id, name, department, salary) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (employee.emp_id, employee.name,
                       employee.department, employee.salary))
        conn.commit()
        conn.close()
        print("✅ Employee added successfully.")

    def view_employees(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            print("⚠️ No employees found.")
            return

        headers = ["ID", "Name", "Department", "Salary"]
        print("\n---- Employee List ----")
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def update_employee(self, emp_id, name=None, department=None, salary=None):
        if not self.employee_exists(emp_id):
            print("❌ Employee ID not found.")
            return

        conn = get_connection()
        cursor = conn.cursor()
        updates = []
        params = []

        if name:
            updates.append("name = %s")
            params.append(name)
        if department:
            updates.append("department = %s")
            params.append(department)
        if salary is not None:
            updates.append("salary = %s")
            params.append(salary)

        if not updates:
            print("⚠️ No fields to update.")
            return

        params.append(emp_id)
        sql = f"UPDATE employees SET {', '.join(updates)} WHERE id = %s"
        cursor.execute(sql, tuple(params))
        conn.commit()
        conn.close()
        print("✅ Employee updated successfully.")

    def delete_employee(self, emp_id):
        if not self.employee_exists(emp_id):
            print("❌ Employee ID not found.")
            return

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id = %s", (emp_id,))
        conn.commit()
        conn.close()
        print("✅ Employee deleted successfully.")

    def search_employee_by_id(self, emp_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE id = %s", (emp_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            print(tabulate([row], headers=["ID", "Name",
                  "Department", "Salary"], tablefmt="grid"))
        else:
            print("❌ Employee not found.")

    def search_employee_by_name(self, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM employees WHERE name LIKE %s", (f"%{name}%",))
        rows = cursor.fetchall()
        conn.close()

        if rows:
            print("\n---- Search Results ----")
            print(tabulate(rows, headers=[
                  "ID", "Name", "Department", "Salary"], tablefmt="grid"))
        else:
            print("❌ No employees found with that name.")

    def count_employees(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM employees")
        total = cursor.fetchone()[0]
        conn.close()
        print(f"📊 Total Employees: {total}")

    def average_salary(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT AVG(salary) FROM employees")
        avg = cursor.fetchone()[0]
        conn.close()
        if avg is not None:
            print(f"💰 Average Salary: ₹{avg:.2f}")
        else:
            print("⚠️ No employees to calculate average salary.")

    def filter_by_department(self, dept_name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM employees WHERE department LIKE %s", (f"%{dept_name}%",))
        rows = cursor.fetchall()
        conn.close()

        if rows:
            print(f"\n---- Employees in '{dept_name}' ----")
            print(tabulate(rows, headers=[
                  "ID", "Name", "Department", "Salary"], tablefmt="grid"))
        else:
            print("❌ No employees found in that department.")
