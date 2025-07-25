# tkinter-database-manager

## 🧾 Warehouse Management System

An application built in Python using the `tkinter` library and a MySQL database. It allows you to manage suppliers, products, customers, invoices, warehouse orders, and sales.

---

## 📦 Application Features

- View and edit data in the database (suppliers, customers, products, etc.)
- Add and delete records from selected tables
- Integration with MySQL database (foreign key relationships and `ON DELETE CASCADE`)
- Graphical interface built with `tkinter`

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** – for the GUI
- **MySQL** – relational database
- **mysql-connector-python** – to connect Python with MySQL

---

## 💾 Requirements

- **Python 3.7** or newer
- **MySQL Server** – installed and configured locally or on a remote host
- Installed Python packages:
  - `mysql-connector-python`
  - `tkinter` (included by default in most Python installations)

---

## 🚀 How to Run

1. Create a database in MySQL (e.g., named `hurtownia`) and load the structure from the provided SQL file.

2. Open `main.py` and enter your database connection details:

    ```python
    db = sql.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="hurtownia"
    )
    ```

3. Run the application:

    ```bash
    python main.py
    ```

4. The application should now be running, allowing you to manage your warehouse data through a user-friendly graphical interface.

---

