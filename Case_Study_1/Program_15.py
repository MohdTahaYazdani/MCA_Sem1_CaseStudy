# Loan EMI Calculator (Simple)

loan_amount = float(input("Enter loan amount: "))
interest_rate = float(input("Enter interest rate (%): "))
loan_period = float(input("Enter loan period (years): "))

total_payment = loan_amount + (loan_amount * interest_rate * loan_period) / 100
emi = total_payment / (loan_period * 12)

print(f"EMI: {emi:.2f}")