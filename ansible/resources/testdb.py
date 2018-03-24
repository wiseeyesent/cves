#!/usr/bin/python
import mysql.connector as mariadb

mdbconn = mariadb.connect(user="testusr", password="!!!MySQLT3stUs3r!!!", database="employees", unix_socket="/var/lib/mysql/mysql.sock")
cursor = mdbconn.cursor()
print("Finding three Georgi's...")
cursor.execute("SELECT * FROM employees WHERE first_name=%s limit 3", ("Georgi",))
for g in cursor:
    print(g)
