# Student Academic Performance Tracker


# Task-1 Store student record in dictionary
student_record = {
    "S101": ("Alice", 85, 80, 88),
    "S102": ("Bob", 87, 93, 95),
    "S103": ("Charlie", 54, 68, 64)
}

# Tasks 2 & 3: calculate average and grade for each student
results = []
for item_id, details in student_record.items(): # details = (item_id, name, average, grade, status)
    name = details[0]
    total = int(details[1]) + int(details[2]) + int(details[3])   # type casting
    average = float(total) / 3

    if average >= 40:                    # nested if-elif-else
        status = "PASS"
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        else:
            grade = "C"
    else:
        status = "FAIL"
        grade = "F"

    results.append((item_id, name, average, grade, status))

# Task 4: sort by average, highest first
results.sort(key=lambda r: r[2], reverse=True)

# Task 5: dashboard
print(50 * "=")
print("ACADEMIC PERFORMANCE DASHBOARD".center(50))
print(50 * "=")
print(f"{'Rank':<4} | {'ID':<4} | {'Name':<7} | {'Average':<7} | {'Grade':<5} | Status")
print(50 * "-")

total_average = 0
for rank, (item_id, name, average, grade, status) in enumerate(results, start=1):
    print(f"{rank:<4} | {item_id:<4} | {name:<7} | {average:<7.2f} | {grade:<5} | {status}")
    total_average += average

class_average = total_average / len(results)
top_student = results[0]

print(50 * "-")
print(f"Class Average Score : {class_average:.2f}")
print(f"Top Scoring Student : {top_student[1]} ({top_student[2]:.2f})")
print(50 * "=")