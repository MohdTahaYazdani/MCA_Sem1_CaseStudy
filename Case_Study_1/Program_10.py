distance = float(input("Enter distance (km): "))
mileage = float(input("Enter mileage (km/litre): "))
fuel_price = float(input("Enter fuel price (per litre): "))

fuel_required = distance / mileage
fuel_cost = fuel_required * fuel_price

print("-" * 50)
print(f"Distance: {distance} km")
print(f"Mileage: {mileage} km/litre")
print(f"Fuel Required: {fuel_required:.2f} litres")
print(f"Fuel Cost: {fuel_cost:.2f}")
print("-" * 50)