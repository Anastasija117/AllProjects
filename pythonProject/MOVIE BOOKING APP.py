# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Default: book is available

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' wasn't borrowed.")

    def __str__(self):
        availability = "Not Available" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} ({availability})"


# Patron Class
class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List to hold borrowed books

    def borrow_book(self, book):
        if book not in self.borrowed_books:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"{self.name} has already borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} hasn't borrowed '{book.title}'.")

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        if borrowed_titles:
            borrowed_books_str = ", ".join(borrowed_titles)
            return f"{self.name} has borrowed: {borrowed_books_str}"
        else:
            return f"{self.name} has no borrowed books."

# Example usage
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

patron1 = Patron("John Doe")

# Borrowing a book
patron1.borrow_book(book1)
print(book1)  # Should show "1984 by George Orwell (Not Available)"

# Attempting to borrow the same book again
patron1.borrow_book(book1)

# Returning the book
patron1.return_book(book1)
print(book1)  # Should show "1984 by George Orwell (Available)"

# Checking the patron's borrowed books
print(patron1)  # Should show "John Doe has no borrowed books."

# Borrowing another book
patron1.borrow_book(book2)
print(patron1)  # Should show "John Doe has borrowed: To Kill a Mockingbird"
print(book2)    # Should show "To Kill a Mockingbird by Harper Lee (Not Available)"
