def get_deduction(prompt, basic_salary, allowances):
    while True:
        deduct = float(input(prompt))

        if deduct > (basic_salary + allowances):
            print("Warning! Deduction exceeds earnings.")
        else:
            return deduct

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
deductions = get_deduction("Enter deductions: ", basic_salary, allowances)

print("-"*50)
print("Employee name: ", employee_name)
print("Basic Salary: ", basic_salary)
print("Allowances: ", allowances)
net_salary = basic_salary + allowances - deductions
print(f"Net Salary: {net_salary:.2f}")