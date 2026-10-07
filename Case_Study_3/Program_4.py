# Banking ATM & Transaction Ledger


# Task-1 Initializing account detail in dictionary
account = {
    'acc_num': 11111111,'name':'Taha', 'pin': 1111, 'balance': 1000,'initial_balance' :1000, 'transaction': []
}

authentification = False
verify_pin = ""

# Task-2 Verify customer PIN
while verify_pin != account["pin"]:
    verify_pin = int(input("Enter your PIN: ").strip())
    if verify_pin == account['pin']:
        authentification = True
        print("PIN Verification Successful")
    else:
        print("PIN Verification Failed")


# Task-3 & 4    Perform Transaction and validate withdrawal limit
if authentification:
    deposit = 250
    account['balance'] += deposit
    account["transaction"].append(('Deposit', deposit))

    withdraw = 100
    if account['balance'] - withdraw >=0:
        account['balance'] -= withdraw
        account["transaction"].append(('Withdraw', withdraw))
    else:
        print("Denied! Insufficient Balance")

# Task-5 Dashboard of 'Bank Account Statement Report
print("="*50)
print(f"{'BANK STATEMENT REPORT':^50}")
print("="*50)
print(f"{'Account Number':<20} : {account['acc_num']:<20}")
print(f"{'Holder Name':<20} : {account['name']:<20}")
print("-"*50)
print(f"{'Type':<18} | {'Amount ($)':<12} | {'Balance ($)':<10}")
print("-"*50)
print(f"{'Initial Balance':<18} | {'':<12} | {account['initial_balance']:.2f}")

new_balance = account['initial_balance']

for transaction_type, amount in account['transaction']:
    if transaction_type == 'Deposit':
        new_balance += amount
    elif transaction_type == 'Withdraw':
        new_balance -= amount

    print(f"{transaction_type:<18} | {amount:<12} | {new_balance:.2f}")

print("-"*50)
print(f"Closing Balance : ${account['balance']:,.2f}")
print("="*50)