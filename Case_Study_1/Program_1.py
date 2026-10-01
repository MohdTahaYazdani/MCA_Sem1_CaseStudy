def get_marks(prompt, maximum):
    while True:
        try:
            marks = float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if marks < 0 or marks > maximum:
            print(f"Invalid marks! Enter a value between 0 and {maximum}.")
        else:
            return marks


student_name = input("Enter student name = ")
maximum_marks = float(input("Enter maximum marks per subject = "))

subject1_marks = get_marks("Enter subject 1 marks = ", maximum_marks)
subject2_marks = get_marks("Enter subject 2 marks = ", maximum_marks)
subject3_marks = get_marks("Enter subject 3 marks = ", maximum_marks)

total_marks = subject1_marks + subject2_marks + subject3_marks
percentage = (total_marks / (maximum_marks * 3)) * 100

print("Student:", student_name)
print("Total Marks:", total_marks)
print(f"Percentage:", round(percentage),"%")
