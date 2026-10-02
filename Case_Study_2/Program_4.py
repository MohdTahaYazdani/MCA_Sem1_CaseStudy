# Student Marksheet

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

english = float(input("Enter marks in English: "))
maths = float(input("Enter marks in Mathematics: "))
computer = float(input("Enter marks in Computer Science: "))
science = float(input("Enter marks in Science: "))
social = float(input("Enter marks in Social Studies: "))

total_marks = english + maths + computer + science + social
average_marks = total_marks / 5

print()
print("=" * 10 + " STUDENT MARKSHEET " + "=" * 10)
print()
print(f"Student Name: {name}")
print(f"Roll Number: {roll_no}")
print()
print(f"English: {english:g}")
print(f"Mathematics: {maths:g}")
print(f"Computer Science: {computer:g}")
print(f"Science: {science:g}")
print(f"Social Studies: {social:g}")
print()
print(f"Total Marks: {total_marks:g}")
print(f"Average Marks: {average_marks:.2f}")
print()
print("=" * 39)