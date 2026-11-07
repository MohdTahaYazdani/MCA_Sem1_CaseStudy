# Experiment 13: University Database Management Dashboard

# Import python library(module) SQlite3 to work with database directly
import sqlite3 as sql

# Connect or create to database if not Exist
conn = sql.connect("University.db")
cur = conn.cursor()   # cursor() is used to execute SQL commands in db.

# Create student table if not exist
cur.execute("""CREATE TABLE IF NOT EXISTS student(
               student_id integer PRIMARY KEY,
               name text,
               department text,
               cgpa real)""")

data = [(101,"Taha","CSE",9.8),
        (102,"Sharif","CS",8.9),
        (103,"Zaid","Comm",8.3),
        (104,"Azam","CA",7.8)]

# Insert data into student table
cur.executemany("""Insert or ignore into student values(?,?,?,?)""",data)
conn.commit()

# Executing Queries
cur.execute("Select count(*) from student")
total = cur.fetchone()[0]

cur.execute("select avg(cgpa) from student")
avg_cgpa = cur.fetchone()[0]

cur.execute("Select name,cgpa from student order by cgpa desc limit 1")
top = cur.fetchone()

# Display University DataBase Dashboard
print("="*50)
print(f"{'UNIVERSITY DATABASE DASHBOARD':^50}")
print("="*50)
print(f"{'Total Students: '} {total}")
print(f"{'Average CGPA: '} {round(avg_cgpa,2)}")
print(f"{'Top Student: '} {top[0]}")
print(f"{'Top CGPA: '} {top[1]}")
print("="*50)