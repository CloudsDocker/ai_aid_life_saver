# ai_aid_life_saver
AI Aid scripts to save your time and life

# MySQL Database Import Script

This script is used to import a MySQL database dump file into a specified database. It uses the `subprocess` module to execute a MySQL command that loads the dump file into the database. 

## Prerequisites
- MySQL installed on your system
- Python 3.x
- `mysql-connector-python` Python module

## How to use
1. Set the database name and the path to the SQL dump file in the `database` and `sql_dump_file` variables, respectively.
2. Set the host, username, and password of your MySQL database in the `host`, `username`, and `password` variables.
3. Run the script using a Python interpreter.

The script will create a new database if it doesn't already exist, create a new user for the database, grant the user all privileges on the database, and then import the SQL dump file into the database.

Note that the `mysql-connector-python` module needs to be installed in order for the script to work. You can install it using pip:

```
pip install mysql-connector-python
```


Please make sure that the MySQL database credentials are correct and that the MySQL server is running before running the script.
