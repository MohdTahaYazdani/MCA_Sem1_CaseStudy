# Experiment 1: University Student Academic Dashboard

# taking student details
student_id = int(input("Enter Student ID: "))
name = input("Enter Student Name: ")
department = input("Enter Department Name: ")

# Taking student's subject marks
total_marks = 0.00
for subject in ["Python","CSA","ST","OS","SE"]:
    total_marks += int(input(f"Enter {subject} Marks: "))

average = total_marks/5
percentage = total_marks*100/500

# Display Dashboard
print("="*50)
print(f"{'UNIVERSITY STUDENT DASHBOARD':^50}")
print("="*50)
print(f"{'Student ID':<10} : {student_id}")
print(f"{'Name':<10} : {name}")
print(f"{'Department':<10} : {department}")
print(f"{'Total':<10} : {total_marks}")
print(f"{'Average':<10} : {average:.2f}")
print(f"{'Percentage':<10} : {percentage:.2f} % ")
print("="*50)