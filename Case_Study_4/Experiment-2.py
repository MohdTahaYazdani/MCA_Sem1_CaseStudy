# Experiment 2: Banking Account Dashboard

# Taking account Details
account = int(input("Please enter  account number: "))
cust_name = str(input("Please enter cust_name: "))
balance = float(input("Enter opening balance: "))

print("1 = Deposit , 2 = withdraw , 3 = balance_inquiry")
choice = int(input("Please enter choice: "))
status = ""

# Perform Transaction
if choice == 1:
    deposit = float(input("Please enter deposit amount: "))
    balance += deposit
    status = "Deposit Successful"
elif choice == 2:
    withdraw = float(input("Please enter withdraw amount: "))
    if withdraw <= balance:
        balance -= withdraw
        status = "Withdraw Successful"
    else:
        status = "Invalid! Enter sufficient balance"
elif choice == 3:
    status = "Balance inquiry Successful"

# Display Dashboard
print("="*50)
print(f"{'BANKING DASHBOARD':^50}")
print("="*50)
print(f"{'Account':<10} : {account}")
print(f"{'Customer':<10} : {cust_name}")
print(f"{'Status':<10} : {status}")
print(f"{'Balance':<10} : ₹ {balance:.1f}")
print("="*50)