# Hospital Patient Priority Queue

# TASK 1: Waiting list as a list of dictionaries
waiting_list = []   # each item: {'name': str, 'age': int, 'is_emergency': bool}


# TASK 2: Insert patients by priority
def add_patient(name, age, is_emergency):
    patient = {'name': name, 'age': int(age), 'is_emergency': is_emergency}
    if is_emergency:
        waiting_list.insert(0, patient)     # emergency goes to the head
        print(f"  CRITICAL patient '{name}' placed at the front of the queue.")
    else:
        waiting_list.append(patient)        # regular goes to the end
        print(f"  Patient '{name}' added to the end of the queue.")


# TASK 3: Dequeue when a doctor is available
def call_next_patient():
    if len(waiting_list) == 0:
        print("  No patients are waiting.")
        return None
    patient = waiting_list.pop(0)
    print(f"  Doctor is ready: calling '{patient['name']}' (age {patient['age']}).")
    return patient


# TASK 4: Average age using a loop and type casting
def average_age():
    if len(waiting_list) == 0:
        return 0.0
    total_age = 0
    for patient in waiting_list:
        total_age += int(patient['age'])         # ensure integer ages
    return float(total_age) / len(waiting_list)  # cast result to float


# TASK 5: Dashboard
def print_dashboard():
    print("=" * 50)
    print("HOSPITAL TRIAGE QUEUE DASHBOARD")
    print("=" * 50)
    print(f"{'Pos':<4}| {'Patient Name':<14}| {'Age':<4}| Priority Status")
    print("-" * 50)
    for position, patient in enumerate(waiting_list, start=1):
        status = "CRITICAL" if patient['is_emergency'] else "REGULAR"
        print(f"{position:<4}| {patient['name']:<14}| {patient['age']:<4}| {status}")
    print("-" * 50)
    print(f"Total Waiting Patients : {len(waiting_list)}")
    print(f"Average Patient Age    : {average_age():.1f} years")
    print("=" * 50)


# Interactive menu
def main():
    while True:
        print("\n----- TRIAGE DESK MENU -----")
        print("1. Add patient")
        print("2. Call next patient")
        print("3. View dashboard")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            name = input("Patient name: ").strip().title()
            try:
                age = int(input("Patient age: "))
            except ValueError:
                print("  Age must be a whole number.")
                continue
            emergency = input("Emergency case? (y/n): ").strip().lower() == 'y'
            add_patient(name, age, emergency)
        elif choice == '2':
            call_next_patient()
        elif choice == '3':
            print_dashboard()
        elif choice == '4':
            print("Exiting triage system.")
            break
        else:
            print("  Invalid choice. Please enter a number from 1 to 4.")


# Demo run matching the expected output
if __name__ == "__main__":
    add_patient("Mary Smith", 29, False)
    add_patient("Alex Brown", 42, False)
    add_patient("John Doe", 64, True)      # jumps to the front
    print()
    print_dashboard()

    main()