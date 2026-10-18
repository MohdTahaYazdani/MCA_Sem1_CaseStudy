# Experiment 7: Restaurant Order Management Dashboard

# Defining Functions
def item_amount(amount , qty):
    return amount * qty
def tax(amount , rate=5):
    return amount * rate / 100
def dashboard(table , subtotal , tax_amount):
    print("="*50)
    print(f"{'RESTAURANT ORDER DASHBOARD':^50}")
    print("="*50)
    print(f"{'Table'} : {table}")
    print(f"{'Subtotal':<10}: ₹ {subtotal}")
    print(f"{'Tax':<10}: ₹ {tax_amount}")
    print(f"{'Total':<10}: ₹ {subtotal + tax_amount}")
    print("="*50)
# Create restaurant menu
menu = {"Biryani":250 , "Juice":80 , "Dessert":120 , "Coffee":60}

# Table wise taking orders
table = input("Enter table number: ")
subtotal = 0
for item,price in menu.items():
    quantity = int(input(f"{item} {'quantity'}: "))
    subtotal += item_amount(price,quantity)

# Calling Functions
tax_amount = tax(subtotal)
dashboard(table , subtotal , tax_amount)
