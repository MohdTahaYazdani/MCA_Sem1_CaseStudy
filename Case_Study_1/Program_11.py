person_name = input("Enter person name: ")
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"


print("-" * 50)
print("Person Name:", person_name)
print(f"Weight in (Kg): {weight} kg")
print(f"Height in (m): {height} m")
print(f"BMI (Body Mass Index): {bmi:.2f}")
print("Category:", category)

print("-" * 50)