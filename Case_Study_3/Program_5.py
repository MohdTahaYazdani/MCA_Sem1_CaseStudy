# Library Catalog & Circulation Desk


# TASK 1: Catalog stored in a dictionary
catalog = {
    'B101': {'title': 'Python Fundamentals',     'author': 'Guido Rossum'},
    'B102': {'title': 'Data Science Essentials', 'author': 'Jane Walker'},
    'B103': {'title': 'Clean Code Principles',   'author': 'Robert Martin'},
}

# TASK 2: Two distinct sets
available_books = set(catalog.keys())   # all books start available
issued_books = set()                    # nothing issued yet


# TASK 3: Issue a book (shifts ID between sets)
def issue_book(book_id):
    if book_id not in catalog:
        print(f"  Error: Book ID '{book_id}' does not exist in the catalog.")
    elif book_id in issued_books:
        print(f"  Sorry, '{catalog[book_id]['title']}' is already issued.")
    else:
        available_books.remove(book_id)
        issued_books.add(book_id)
        print(f"  Success: '{catalog[book_id]['title']}' has been issued.")


# TASK 4: Handle returns
def return_book(book_id):
    if book_id not in catalog:
        print(f"  Error: Book ID '{book_id}' does not exist in the catalog.")
    elif book_id in available_books:
        print(f"  '{catalog[book_id]['title']}' is already in the library.")
    else:
        issued_books.remove(book_id)
        available_books.add(book_id)
        print(f"  Success: '{catalog[book_id]['title']}' has been returned.")


# TASK 5: Dashboard
def print_dashboard():
    print("=" * 50)
    print("LIBRARY CATALOG STATUS DASHBOARD")
    print("=" * 50)
    print(f"{'ID':<5}| {'Book Title':<24}| Status")
    print("-" * 50)
    for book_id in sorted(catalog):
        status = "AVAILABLE" if book_id in available_books else "ISSUED"
        print(f"{book_id:<5}| {catalog[book_id]['title']:<24}| {status}")
    print("-" * 50)
    print(f"Total Catalog Books : {len(catalog)}")
    print(f"Available Copies    : {len(available_books)}")
    print(f"Issued Copies       : {len(issued_books)}")
    print("=" * 50)


# TASK 3: Menu dispatching with if-elif-else
def main():
    while True:
        print("\n----- CIRCULATION DESK MENU -----")
        print("1. Issue a book")
        print("2. Return a book")
        print("3. View dashboard")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            issue_book(input("Enter Book ID to issue: ").strip().upper())
        elif choice == '2':
            return_book(input("Enter Book ID to return: ").strip().upper())
        elif choice == '3':
            print_dashboard()
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter a number from 1 to 4.")


# Demo run matching the expected output
if __name__ == "__main__":
    # Automatic demo: issue B102, then show the dashboard
    issue_book('B102')
    # print()
    print_dashboard()

    main()