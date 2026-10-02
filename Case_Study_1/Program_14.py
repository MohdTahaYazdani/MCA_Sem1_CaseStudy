# Bank Account Balance Calculator

customer_name = input("Enter customer name: ")
current_balance = float(input("Enter current balance: "))
deposit_amount = float(input("Enter deposit amount: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

updated_balance = current_balance + deposit_amount - withdrawal_amount

print("Customer Name:", customer_name)
print(f"Updated Balance: {updated_balance:.2f}")