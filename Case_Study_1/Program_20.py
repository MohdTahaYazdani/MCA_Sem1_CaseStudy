# Profit or Loss

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

profit_or_loss = selling_price - cost_price

if profit_or_loss > 0:
    print(f"Profit: {profit_or_loss:.2f}")
elif profit_or_loss < 0:
    print(f"Loss: {abs(profit_or_loss):.2f}")
else:
    print("No Profit, No Loss")