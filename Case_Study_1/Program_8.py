item_name = input("Enter item name: ")
item_quantity = int(input("Enter item quantity: "))
price_per_item = float(input("Enter price of one item: "))


amount = item_quantity * price_per_item

print("-"*50)
print("Item name: ", item_name)
print("Item quantity: ", item_quantity)
print("amount:", amount)