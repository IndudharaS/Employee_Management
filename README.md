# 📘 Employee Management System

A simple **console-based Python application** to manage employees using **MySQL** for storage. No frameworks (like Django or Flask) are used—this is a raw and educational CRUD project perfect for learning Python and MySQL integration using `mysql-connector-python`.

---

## 🔧 Features

- ✅ Add Employee (with duplicate ID check)
- 📋 View All Employees (formatted table view)
- ✏️ Update Employee Details (name, department, or salary)
- ❌ Delete Employee
- 🔍 Search by ID or Name
- 🧮 Show Total Employees
- 💰 Calculate Average Salary
- 🗂️ Filter Employees by Department

---

## 🛠️ Technologies Used

- **Python 3.x**
- **MySQL Workbench / MySQL Server**
- **VS Code**
- `mysql-connector-python` (for database connection)
- `tabulate` (for table-style display)

---

## 📂 Project Structure

```
employee_management/
│
├── employee.py            # Employee data class
├── employee_dao.py        # Contains all database operations
├── db_config.py           # MySQL database connection
├── main.py                # Main driver with menu system
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. 🐍 Install Python Packages

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```
mysql-connector-python
tabulate
```

### 2. 🛢️ Setup MySQL Database

Log in to **MySQL Workbench** and run:

```sql
CREATE DATABASE IF NOT EXISTS employee_db;

USE employee_db;

CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary FLOAT
);
```

### 3. 🛠️ Configure Database Connection

Edit `db_config.py`:

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="your_mysql_password",
        database="employee_db"
    )
```

Replace `your_mysql_username` and `your_mysql_password` with your actual MySQL credentials.

---

## ▶️ Run the Application

```bash
python main.py
```

You will see a menu in the terminal:

```
==== Employee Management System ====
1. Add Employee
2. View All Employees
3. Update Employee
4. Delete Employee
...
```

---

## ✅ Sample Actions

- Add an employee → ID, Name, Department, Salary
- View employees → Shows all in a neat table
- Update → Only fields you want to change
- Search by ID or partial name
- Filter by department
- View total and average salary stats

---

## 📌 Notes

- The ID field must be **unique**.
- Ensure MySQL server is running when using the app.
- All data is stored in the MySQL `employee_db.employees` table.

---

## 📬 Author

Developed by **Indudhara S**
