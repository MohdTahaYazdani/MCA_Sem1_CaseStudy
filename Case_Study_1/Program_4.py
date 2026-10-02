emp_name = input("Enter employee name: ")
basicSalary = float(input("Enter basic salary: "))

hra_percent = float(input("Enter (hra %) based on Basic Salary: "))
da_percent = float(input("Enter (da %) based on Basic Salary: "))

hra = (basicSalary * hra_percent) / 100
da = (basicSalary * da_percent) / 100

gross_salary = basicSalary + hra + da

print ("-"*50)

print("Employee name: ", emp_name)
print("Basic Salary: ", basicSalary)
print("Hra percent: ", hra)
print("Da percent: ", da)
print("Gross Salary: ", gross_salary)