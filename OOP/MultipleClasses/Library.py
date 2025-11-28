class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


    def borrow(self, book):
        self.borrowed_books.append(book)


class Library:
    def __init__(self):
        self.books = []


    def add_book(self, book):
        self.books.append(book)


    def show_borrowed(self, member):
        print(f"\n{member.name} borrowed:")
        for book in member.borrowed_books:
            print(f"- {book.title} by {book.author}")
        print("====================================")



# Driver Code
lib = Library()
b1 = Book("1984", "George Orwell")
b2 = Book("To Kill a Mockingbird", "Harper Lee")
b3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
m1 = Member("Joy")
m2 = Member("Mumita")
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
m1.borrow(b1)
m1.borrow(b2)
m2.borrow(b3)

lib.show_borrowed(m1)
lib.show_borrowed(m2)