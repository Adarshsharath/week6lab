def read_books():
    books = []
    with open("books.txt", "r") as file:
        for line in file:
            book_id, title, author, category, status = line.strip().split(",")
            books.append({
                "Book_ID": int(book_id),
                "Title": title,
                "Author": author,
                "Category": category,
                "Status": status
            })
    return books

# Function to write updated book list back to the file
def write_books(books):
    with open("books.txt", "w") as file:
        for book in books:
            file.write(f"{book['Book_ID']},{book['Title']},{book['Author']},{book['Category']},{book['Status']}\n")

# Function to view all books
def view_books():
    books = read_books()
    if books:
        for book in books:
            print(f"ID: {book['Book_ID']}, Title: {book['Title']}, Author: {book['Author']}, Category: {book['Category']}, Status: {book['Status']}")
    else:
        print("No books available.")

# Function to search for books based on different fields
def search_books(field, value):
    books = read_books()
    results = []
    
    for book in books:
        if book[field].lower() == value.lower():
            results.append(book)
    
    if results:
        for book in results:
            print(f"ID: {book['Book_ID']}, Title: {book['Title']}, Author: {book['Author']}, Category: {book['Category']}, Status: {book['Status']}")
    else:
        print(f"No books found matching {field}: {value}")

# Function to delete a book by Book ID
def delete_book(book_id):
    books = read_books()
    books_to_delete = [book for book in books if book['Book_ID'] == book_id]
    
    if books_to_delete:
        books = [book for book in books if book['Book_ID'] != book_id]
        write_books(books)
        print(f"Book with ID {book_id} has been deleted.")
    else:
        print(f"Book with ID {book_id} not found.")

# Main function to interact with the user
def main():
    while True:
        print("\n1. View all books")
        print("2. Search for a book")
        print("3. Delete a book")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_books()
        elif choice == "2":
            field = input("Search by (Title, Author, Category): ").strip()
            value = input(f"Enter the {field}: ").strip()
            if field.lower() in ['title', 'author', 'category']:
                search_books(field.capitalize(), value)
            else:
                print("Invalid field. Please choose Title, Author, or Category.")
        elif choice == "3":
            try:
                book_id = int(input("Enter the Book ID to delete: ").strip())
                delete_book(book_id)
            except ValueError:
                print("Invalid input. Please enter a valid Book ID.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()