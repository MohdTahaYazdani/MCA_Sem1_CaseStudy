# Experiment 4: Supermarket & Shopping Mall Dashboard

subtotal = 0
discount = 0
final_bill = 0
item = 0

# Add multiple supermarket products on bill
while True:
    product = str(input("Please enter product name: "))
    if product.lower().strip() == "done":
        break
    else:
        quantity = int(input("Please enter quantity: "))
        if quantity > 0:
            price = float(input("Please enter price per unit: "))
            item += 1
        else:
            continue

    subtotal += price * quantity

# Apply discount according to the bill
if subtotal >= 5000:
    discount = subtotal *10/ 100
elif subtotal >= 1000:
    discount = subtotal * 5/ 100
else:
    discount = 0

total_bill = subtotal - discount

# Display Sales Dashboard
print("="*50)
print(f"{'SUPERMARKET & SHOPPING MALL':^50} \n {'SALES DASHBOARD':^50}")
print("="*50)
print(f"{'Item'} : {item}")
print(f"{'Subtotal'} : ₹ {subtotal:.2f}")
print(f"{'Discount'} : ₹ {discount:.2f}")
print(f"{'Final'} : ₹ {total_bill:.2f}")
print("="*50)
