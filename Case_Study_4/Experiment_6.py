# Experiment 6: Airport Passenger Management Dashboard


# Initializing the string
passengers = []
# Perform the operations
while True:
    print("1=Add , 2=Remove , 3=Search , 4=Sort , 5=Dashboard , 6=Exit")
    choice = int(input("Enter your choice:"))
# Add passengers
    if choice == 1:
        passengers.append(input("Enter passenger name:").capitalize())
# Remove passengers
    elif choice == 2:
        name = input("Enter passenger name to remove:").capitalize()
        if name in passengers:
            passengers.remove(name)
        else:
            print("Passenger is not found")
# Search passengers
    elif choice == 3:
        search = input("Enter passenger name to search:").capitalize()
        for passenger in passengers:
            if passenger == search:
                print("Passenger is found")
                break
            else:
                print("Passenger is not found")
                break
# Sort passengers
    elif choice == 4:
        passengers.sort()
# Display Dashboard
    elif choice == 5:
        print("="*50)
        print(f"{'AIRPORT PASSENGER DASHBOARD':^50}")
        print("="*50)
        print(f"{'Total Passengers'} : {len(passengers)}")
        for passenger,p in enumerate(passengers,1):
            print(f"{passenger} . {p}")
        print("="*50)
#Exit from string
    elif choice == 6:
        break