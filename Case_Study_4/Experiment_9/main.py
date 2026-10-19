# Experiment 9: University Administration Dashboard – Modules & Packages

# Importing modules from other files
from student import *
from admission import *
from placement import *

# Display Dashboard
print("="*50)
print(f"{'UNIVERSITY ADMIN DASHBOARD':^50}")
print("="*50)
print(f"{'Students'} : {student_count()}")
print(f"{'Admissions'} : {admission_count()}")
print(f"{'Placed'} : {placed_count()}")
print("="*50)