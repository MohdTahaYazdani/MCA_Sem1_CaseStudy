consumer_name = input("Enter consumer name: ")
water_unit = float(input("Enter water unit: "))
rate_per_unit = float(input("Enter rate per unit: "))

water_bill = water_unit * rate_per_unit

print(f"Water Bill: {water_bill:.2f}")