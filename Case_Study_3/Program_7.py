# Movie Theater Seat Reservation Engine

ROWS = 3
COLS = 4

# TASK 1: 3x4 seat matrix (False = Vacant, True = Booked)
seats = [[False for _ in range(COLS)] for _ in range(ROWS)]


# TASK 2: Booking routine with availability check
def book_seat(row, col):
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        print(f"  Error: Seat ({row}, {col}) does not exist. "
              f"Rows are 0-{ROWS - 1}, columns are 0-{COLS - 1}.")
    elif seats[row][col]:
        print(f"  Sorry, seat (Row {row}, Col {col}) is already booked.")
    else:
        seats[row][col] = True
        print(f"  Success: seat (Row {row}, Col {col}) has been booked.")


# TASK 3: Metrics using list iteration
def compute_metrics():
    total = 0
    booked = 0
    for row in seats:
        for seat in row:
            total += 1
            if seat:
                booked += 1
    occupancy = (booked / total) * 100
    return total, booked, occupancy


# TASK 5: Dashboard
def print_dashboard():
    total, booked, occupancy = compute_metrics()

    print("=" * 50)
    print("THEATER OCCUPANCY DASHBOARD")
    print("=" * 50)
    print("Grid Layout ([ ] = Empty, [X] = Booked):")
    for r in range(ROWS):
        cells = ["[X]" if seat else "[ ]" for seat in seats[r]]
        print(f"Row {r}: " + " ".join(cells))
    print("-" * 50)
    print(f"Total Seats    : {total}")
    print(f"Booked Seats   : {booked}")
    print(f"Occupancy Rate : {occupancy:.1f}%")
    print("=" * 50)


# TASK 4: Interactive menu with if-elif-else
def main():
    while True:
        print("\n----- CINEMA BOOKING MENU -----")
        print("1. Book a seat")
        print("2. View theater map")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            try:
                row = int(input(f"Enter row (0-{ROWS - 1}): "))
                col = int(input(f"Enter column (0-{COLS - 1}): "))
            except ValueError:
                print("  Please enter whole numbers only.")
                continue
            book_seat(row, col)
        elif choice == '2':
            print_dashboard()
        elif choice == '3':
            print("Exiting booking system. Enjoy the movie!")
            break
        else:
            print("  Invalid choice. Please enter 1, 2, or 3.")


# Demo run matching the expected output
if __name__ == "__main__":
    book_seat(0, 0)
    book_seat(0, 3)
    book_seat(1, 1)
    book_seat(1, 1)     # double booking attempt, gets blocked
    print()
    print_dashboard()

    main()