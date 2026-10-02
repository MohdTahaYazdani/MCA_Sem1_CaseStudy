consumer_name = input("Enter consumer name = ")
units_consumed = float(input("Enter units consumed = "))

if units_consumed <= 100:
    bill_amount = units_consumed * 3
elif units_consumed <= 200:
    bill_amount = 100 * 3 + (units_consumed - 100) * 5
else:
    bill_amount = 100 * 3 + 100 * 5 + (units_consumed - 200) * 7

print(f"Bill Amount: {bill_amount:.2f}")