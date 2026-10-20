# # Experiment 11: Festival & National Event File Dashboard

filename = "event_participants.txt"

# Consider the number of participants with exception/error handling
while True:
    try:
        n = int(input("Enter the number of participants: "))
        if n >= 0:
            break
        print("Enter a positive number: ")
    except ValueError:
        print("Enter a valid number: ")

# Open file to write something and (it will close by Default)
with open(filename, "w") as f:  # ("w"= Erase all previous data and start writing) ("a"= start writing without erasing previous data)
    for i in range(n):
        name = input("Name: ").strip().title()
        institution = input("Institute: ").strip().upper()
        f.write(f"{name:<7} | {institution}\n")

# Open file to read all the data of the file and (it will close by Default)
with open(filename, "r") as f: # ("r"= Only read the file & file must be to exist otherwise it throws FileNotFoundError)
    record = f.readlines()

# Display the File Data within the dashboard
print("="*50)
print(f"{'NATIONAL EVENT DASHBOARD':^50}")
print("="*50)
print("Total Registrations: ", len(record))
for i,r in enumerate(record,1):
    print(f"{i} {r.strip()}")
print("="*50)