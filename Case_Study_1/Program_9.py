customer_name = input("Enter customer name: ")
food_bill = float(input("Enter food bill: "))
gst_percentage = float(input("Enter gst percentage: "))

gst_amount = (food_bill * gst_percentage) / 100
final_bill = food_bill + gst_amount

print("-"*50)
print("Customer Name:", customer_name)
print(f"Food Bill: {food_bill:.2f}")
print(f"GST Amount: {gst_amount:.2f}")
print(f"Total Amount: {final_bill:.2f}")