class Library:
    def __init__(self, name, availableBooks):
        self.__name = name
        self.__availableBooks = availableBooks
        self.__borrowerInfo = {}

    def SetborrowerInfo(self, name, books):
        self.__borrowerInfo [name] = books


    def getBooks(self):
        return self.__availableBooks

    def setBookQuantity(self, book_name):
        self.__availableBooks [book_name] = self.__availableBooks [book_name]-1


    def details(self):
        print(f"""Dhaka Library details
Borrower details:
{self.__borrowerInfo}
Books availability:
{self.__availableBooks}""" )


class Reader:
    def __init__(self, name):
        self.name = name
        self.borrowed_book = {}
        self.books = 0


    def borrow(self, loc, *books):
        for book in books:
            if self.books < 5:
                for remaainBook, quantity in loc.getBooks().items():
                    if remaainBook == book:
                        if quantity != 0:
                            if book not in self.borrowed_book:
                                self.borrowed_book[book] = 1


                            else:
                                self.borrowed_book[book] += 1
                                self.books += 1

                                loc.setBookQuantity(book)
                                print(f"{book} book is borrowed successfully.")

                    else:
                        print(f"{book} books are not available at the moment.")
            else:
                print(f"You cannot borrow more than 5 books.")
                break
        loc.SetborrowerInfo(self.name, self.books)


    def readerInfo(self, bookName = None):
        if bookName == None:
            print(f"{self.name}, you have {self.books} book(s) with you.")
            for book, quantity in self.borrowed_book.items():
                print(f"Books on {book}: {quantity}")

        else:
            print(f"{self.name}, you have {self.borrowed_book[bookName]} {bookName} book(s) with you.")





L1=Library('Dhaka',{'Arts':15,'Fiction':135,'Politics':2,'Science':11,'Poetry':15})
L1.details()
print("1----------------------")
r1=Reader('Aladdin')
r1.borrow(L1,'Arts','Fiction','Fiction','Politics')
print("2----------------------")
r1.borrow(L1,'Politics','Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2=Reader('Jasmine')
r2.borrow(L1,'Politics','Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()