# E-Commerce Inventory & Stock Ledger

# Task-1  Creating nested Dictionary
inventory = {
    101: {'name': 'Laptop', 'price': 800.00, 'stock': 10},
    102: {'name': 'Mouse', 'price': 25.00, 'stock': 45},
    103: {'name': 'Keyboard', 'price': 50.00, 'stock': 12.00}
}

# Task-3 Update the stock & Validate the sufficient stock
def purchase(item_id, stock):
    if item_id in inventory and inventory[item_id]['stock'] >= stock:
        inventory[item_id]['stock'] -= stock
    else:
        print(f"\n{item_id} is not in the inventory or invalid stock.")

# Purchase order by the user
purchase(101, 2)


# Initializing the variables & Stock Threshold
stock_threshold = 10
total_valuation = 0
low_stock_count = 0


# Printing Dashboard
print("="*50)
print(f"{'E-COMMERCE STOCK REPORT':^50}")
print("="*50)
print(f"{'ID':<4} | {'Name':<10} | {'Price':<10} | {'Stock':<5} | {'Status':<10}")
print("-"*50)


# Intrying data from nested dictionary
for item_id, details in inventory.items():
    name = details['name']
    price = details['price']
    stock = details['stock']


    # Task-4 Calculate Total inventory Valuation
    total_valuation += (price*stock)

    # task-2 Assigning the status according to stock
    if stock == 0:
        status = "Out of Stock"
        low_stock_count += 1
    elif stock < stock_threshold:
        status = "Low Stock"
        low_stock_count += 1
    else:
        status = "In Stock"

    # Printing The Enteries
    print(f"{item_id:<4} | {name:<10} | {price:<10} | {stock:<5} | {status:<10}")

print("-"*50)
print(f"Total Inventory Valuation: {total_valuation}")
print(f"Low Stock Items Count: {low_stock_count}")
print("="*50)