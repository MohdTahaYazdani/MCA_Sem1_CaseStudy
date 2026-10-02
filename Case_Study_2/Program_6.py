# Case Study 1 - Student Result Dashboard

# Assumed maximum marks (change these if your college uses different values)
MAX_INTERNAL = 20
MAX_ASSIGNMENT = 10
MAX_MIDTERM = 20
MAX_ENDSEM = 50
MAX_TOTAL = MAX_INTERNAL + MAX_ASSIGNMENT + MAX_MIDTERM + MAX_ENDSEM  # 100

MIN_ATTENDANCE = 75   # minimum attendance % to be eligible
MIN_PERCENTAGE = 40   # minimum percentage to pass

# Input
name = input("Enter student name: ")
internal = float(input(f"Enter internal marks (out of {MAX_INTERNAL}): "))
assignment = float(input(f"Enter assignment marks (out of {MAX_ASSIGNMENT}): "))
midterm = float(input(f"Enter mid-term marks (out of {MAX_MIDTERM}): "))
endsem = float(input(f"Enter end-semester marks (out of {MAX_ENDSEM}): "))
attendance = float(input("Enter attendance percentage: "))

# Calculations
total = internal + assignment + midterm + endsem
percentage = (total / MAX_TOTAL) * 100

# Grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= MIN_PERCENTAGE:
    grade = "E"
else:
    grade = "F"

# Examination eligibility
if attendance >= MIN_ATTENDANCE and percentage >= MIN_PERCENTAGE:
    eligibility = "Eligible for Examination"
elif attendance < MIN_ATTENDANCE:
    eligibility = "Not Eligible (Low Attendance)"
else:
    eligibility = "Not Eligible (Low Marks)"

# Output
print()
print("=" * 10 + " STUDENT RESULT DASHBOARD " + "=" * 10)
print()
print(f"Student Name    : {name}")
print()
print(f"Internal        : {internal:g}/{MAX_INTERNAL}")
print(f"Assignment      : {assignment:g}/{MAX_ASSIGNMENT}")
print(f"Mid-Term        : {midterm:g}/{MAX_MIDTERM}")
print(f"End-Semester    : {endsem:g}/{MAX_ENDSEM}")
print(f"Attendance      : {attendance:g}%")
print()
print(f"Total Marks     : {total:g}/{MAX_TOTAL}")
print(f"Percentage      : {percentage:.2f}%")
print(f"Grade           : {grade}")
print(f"Eligibility     : {eligibility}")
print()
print("=" * 46)