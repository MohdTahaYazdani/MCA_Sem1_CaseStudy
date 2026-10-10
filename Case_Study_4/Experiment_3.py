# Experiment 3: Hospital & Diagnostic Centre Dashboard

# Enter Patient Details
patient_id = input("Enter Patient ID: ")
patient_name = input("Enter Patient Name: ")

# Preference of Room type
print("Types of Rooms : G=General, P=Private , A=AC+private ")
room = str(input("Enter Room type: ")).upper().strip()
room_charge = 0
if room == "G":
    room_charge= 1000
elif room == "P":
    room_charge = 2000
elif room == "A":
    room_charge = 4000
else:
    print("Enter valid room type")

# Gathering Additional Charges
days = int(input("Enter Days patient admitted in hospital : "))
doctor_charge = int(input("Enter Doctor charge per day: "))
diagnostic_charge = int(input("Enter Diagnostic charge: "))
medicine_charge = int(input("Enter Medicine charge: "))

room_charge = room_charge * days
doctor_charge = doctor_charge * days
total_bill = room_charge + doctor_charge + diagnostic_charge + medicine_charge

# 10 %  Discount on total bill
discount = float(total_bill*10/100)
net_amount = total_bill - discount

# Display Patient bill dashboard
print("="*50)
print(f"{'HOSPITAL & DIAGNOSTIC DASHBOARD':^50}")
print("="*50)
print(f"{'Patient'} : {patient_id} {patient_name} ")
print(f"{'Room Charges'} : ₹ {room_charge}")
print(f"{'Total Bill':<10} : ₹ {total_bill}")
print(f"{'Discount':<10} : ₹ {discount}")
print(f"{'Net Amount':<10} : ₹ {net_amount}")
print("="*50)