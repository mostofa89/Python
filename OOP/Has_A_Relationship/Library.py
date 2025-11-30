# Component classes
class Book:

    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.available_copies = copies
    

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    

    def return_book(self):
        if self.available_copies < self.copies:
            self.available_copies += 1
    

    def get_info(self):
        return f"'{self.title}' by {self.author} (Available: {self.available_copies}/{self.copies})"


class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
    
    def get_info(self):
        return f"Member: {self.name} (ID: {self.member_id})"


class Librarian:

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    

    def get_info(self):
        return f"Librarian: {self.name} (ID: {self.employee_id})"


# Main class with Has-A relationships
class Library:
    # Library HAS-A collection of Books
    # Library HAS-A collection of Members
    # Library HAS-A Librarian
    def __init__(self, name):
        self.name = name
        self.books = []  # List of Book objects
        self.members = []  # List of Member objects
        self.librarian = None
    

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.get_info()}")
    

    def add_member(self, member):
        self.members.append(member)
        print(f"Registered: {member.get_info()}")
    

    def set_librarian(self, librarian):
        self.librarian = librarian
        print(f"Assigned: {librarian.get_info()}")
    

    def borrow_book(self, book_title, member_name):
        for book in self.books:
            if book.title == book_title:
                if book.borrow():
                    print(f"\n {member_name} borrowed '{book_title}'")
                    print(f"  {book.get_info()}")
                    return
                else:
                    print(f"\n Sorry, '{book_title}' is not available")
                    return
        print(f"\n Book '{book_title}' not found in library")
    

    def display_library(self):
        print(f"\n{'='*60}")
        print(f"Library: {self.name}")
        if self.librarian:
            print(f"{self.librarian.get_info()}")
        
        print(f"\nTotal Books: {len(self.books)}")
        for book in self.books:
            print(f"  - {book.get_info()}")
        
        print(f"\nTotal Members: {len(self.members)}")
        for member in self.members:
            print(f"  - {member.get_info()}")
        print('='*60)


# Testing
print("=== Library Has-A Relationship Demo ===\n")

# Create library
library = Library("City Central Library")

# Add librarian (Library HAS-A Librarian)
library.set_librarian(Librarian("Emma Wilson", "LIB001"))

# Add books (Library HAS-A Books)
library.add_book(Book("Python Programming", "John Doe", "978-1234567890", 3))
library.add_book(Book("Data Science Basics", "Jane Smith", "978-0987654321", 2))
library.add_book(Book("Web Development", "Bob Johnson", "978-1122334455", 4))

print()

# Add members (Library HAS-A Members)
library.add_member(Member("Alice Brown", "MEM001"))
library.add_member(Member("Charlie Davis", "MEM002"))

# Display library info
library.display_library()

# Borrow books
library.borrow_book("Python Programming", "Alice Brown")
library.borrow_book("Python Programming", "Charlie Davis")
library.borrow_book("Data Science Basics", "Alice Brown")