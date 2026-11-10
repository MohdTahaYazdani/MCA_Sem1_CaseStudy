# Experiment 14: Placement, Training & Alumni Database Dashboard


# Import sqlite3 for sql queries.
import sqlite3 as sql

# Create the temporary database in sql and connect with the
conn = sql.connect(":memory:")
cur = conn.cursor()

# Creating tables (Placement , Training , Alumni)
cur.execute("""Create table placement(
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company text not null,
            package real not null
            )""")
cur.execute("""Create table training(
            student_id INTEGER not null unique,
            program_name text not null,
            no_of_students integer not null,
            foreign key (student_id) references placement(student_id)
            )""")
cur.execute("""Create table alumni(
            student_id INTEGER not null unique,
            year integer,
            foreign key (student_id) references placement(student_id)
            )""")

# Inserting values into tables With the help of Exception Handling.
try:
    cur.executemany("INSERT INTO placement(company,package) values(?,?)",
                [("tech_corp", 12.5),("Mahindra_corps",14.5)])

    cur.execute("INSERT INTO training(student_id, program_name, no_of_students) values(?,?,?)",
                (1, "Python with AI/ML", 150))

    cur.execute("INSERT INTO alumni(student_id, year) values(?,?)",
                (3, 2026))

    # Commit the values who have inserted in tables.
    conn.commit()

except sql.IntegrityError as e:
    print(f"Integrity Error - transaction Rolled back: {e} ")
except sql.Error as e:
    print(f"Database Error - Transaction Rolled back: {e} ")


# Statistics for transactions.
cur.execute("Select count(*) from placement")
count_placed = cur.fetchone()[0]

cur.execute("Select no_of_students from training")
no_of_trained = cur.fetchone()[0]

cur.execute("Select student_id from alumni")
count_alumni = cur.fetchone()[0]

cur.execute("Select max(package) from placement")
max_package = cur.fetchone()[0]


# Display Placement/Training & Alumni Dashboard
line = "="*50
print(line)
print(f"{'PLACEMENT, TRAINING & ALUMNI':^50} \n {'DASHBOARD':^50}")
print(line)
print(f"Students Placed   : {count_placed}")
print(f"Students Trained  : {no_of_trained}")
print(f"Registered Alumni : {count_alumni}")
print(f"Highest Package   : {max_package}")
print(line)

conn.close()