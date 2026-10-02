# Challenge 1 - Restaurant Bill Generator

customer = input("Enter customer name: ")

item1 = input("Enter item 1 name: ")
price1 = float(input("Enter item 1 price: "))
qty1 = int(input("Enter quantity of item 1: "))

item2 = input("Enter item 2 name: ")
price2 = float(input("Enter item 2 price: "))
qty2 = int(input("Enter quantity of item 2: "))

item3 = input("Enter item 3 name: ")
price3 = float(input("Enter item 3 price: "))
qty3 = int(input("Enter quantity of item 3: "))

amount1 = price1 * qty1
amount2 = price2 * qty2
amount3 = price3 * qty3
total_bill = amount1 + amount2 + amount3

print()
print("=" * 10 + " RESTAURANT BILL " + "=" * 10)
print()
print(f"Customer Name: {customer}")
print()
print(f"Item 1: {item1}")
print(f"Quantity: {qty1}")
print(f"Amount: {amount1:.2f}")
print()
print(f"Item 2: {item2}")
print(f"Quantity: {qty2}")
print(f"Amount: {amount2:.2f}")
print()
print(f"Item 3: {item3}")
print(f"Quantity: {qty3}")
print(f"Amount: {amount3:.2f}")
print()
print(f"Total Bill: {total_bill:.2f}")
print("=" * 36)