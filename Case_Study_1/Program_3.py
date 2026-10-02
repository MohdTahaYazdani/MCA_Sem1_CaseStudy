principle = float(input("Enter Principle amount: "))
rate = float(input("Enter the Rate of interest (in %): "))
time = float(input("Enter the Time period (in years): "))

amount = principle*(1+(rate/100))**time
CI = amount - principle

print(f"Amount: {amount:.2f}")
print(f"Compound Interest: {CI:.2f}")