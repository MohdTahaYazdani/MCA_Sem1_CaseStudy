# Restaurant Point of Sale (POS) & Billing

TAX_RATE = 0.08
DISCOUNT_THRESHOLD = 50
DISCOUNT_AMOUNT = 5

# TASK 1: Menu dictionary {item_code: (item_name, price)}
menu = {
    1: ('gourmet burger', 12.50),
    2: ('garlic fries',    5.00),
    3: ('soda',            2.50),
    4: ('caesar salad',    9.00),
}


def show_menu():
    print("\n--------- MENU ---------")
    for code, (name, price) in menu.items():
        print(f"{code}. {name.title():<16} ${price:>6.2f}")
    print("0. Finish order")


# TASK 2: Collect orders in a while loop
def take_order():
    order_list = []                       # list of (item_name, quantity, total)
    while True:
        show_menu()
        try:
            code = int(input("Enter item code 1-4 (0 to finish): "))
        except ValueError:
            print("  Please enter a valid number.")
            continue

        if code == 0:
            break
        elif code in menu:
            try:
                qty = int(input("Enter quantity: "))
            except ValueError:
                print("  Please enter a valid quantity.")
                continue
            if qty <= 0:
                print("  Quantity must be at least 1.")
                continue

            name, price = menu[code]
            # TASK 4: standardized formatting with .title()
            order_list.append((name.title(), qty, price * qty))
            print(f"  Added {qty} x {name.title()}")
        else:
            print("  Invalid item code.")
    return order_list


# TASK 3: Subtotal, tax, discount
def calculate_bill(order_list):
    subtotal = sum(item[2] for item in order_list)
    tax = subtotal * TAX_RATE

    if subtotal > DISCOUNT_THRESHOLD:
        discount = DISCOUNT_AMOUNT
    else:
        discount = 0

    final_amount = subtotal + tax - discount
    return subtotal, tax, discount, final_amount


# TASK 5: Print the receipt
def print_receipt(order_list):
    subtotal, tax, discount, final_amount = calculate_bill(order_list)

    print("=" * 50)
    print("GOURMET BISTRO RECEIPT".upper())          # TASK 4: .upper()
    print("=" * 50)
    print(f"{'Item':<16}| {'Qty':<4}| {'Unit Price':<11}| Total ($)")
    print("-" * 50)
    for name, qty, total in order_list:
        unit_price = total / qty
        print(f"{name:<16}| {qty:<4}| ${unit_price:<10.2f}| ${total:.2f}")
    print("-" * 50)
    print(f"{'Subtotal':<13}: ${subtotal:.2f}")
    print(f"{'Tax (8%)':<13}: ${tax:.2f}")
    if discount > 0:
        print(f"{'Discount':<13}:-${discount:.2f}")
    print(f"{'Final Amount':<13}: ${final_amount:.2f}")
    print("=" * 50)


# Main program
if __name__ == "__main__":
    orders = take_order()
    if orders:
        print()
        print_receipt(orders)
    else:
        print("No items ordered.")