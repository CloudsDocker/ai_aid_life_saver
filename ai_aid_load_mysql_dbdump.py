import subprocess

import mysql.connector

database = "unifyxp_test2"
sql_dump_file = "/Users/todd.zhang/Downloads/db-dump-t-2023-05-04-by-expect.sql"
# Connect to the MySQL database
host = "localhost"
username = "root"
password = "root"
conn = mysql.connector.connect(
    host=host,
    user=username,
    password=password
)

# Create a new user with a password
cur = conn.cursor()
cur.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
cur.execute("CREATE USER IF NOT EXISTS 'myuser'@'localhost' IDENTIFIED BY 'myuser';")
cur.execute(f"GRANT ALL PRIVILEGES ON {database}.* TO 'unifyxp'@'localhost';")
conn.commit()
cur.close()

# Construct the MySQL command to import the SQL dump file
mysql_cmd = f"mysql -u {username} -p{password} -h {host} {database} < {sql_dump_file}"

# Execute the MySQL command using subprocess
subprocess.call(mysql_cmd, shell=True)

# Close the database connection
conn.close()
