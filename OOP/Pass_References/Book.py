class Book:
    def __init__(self, title, pages, genre="Fiction"):
        self.title = title
        self.pages = pages
        self.genre = genre


    def printDetails(self):
        print(f"{self.title}: {self.pages} pages, Genre: {self.genre}")


    def merge(self, *books):
        for b in books:
            self.pages += b.pages
            if b.genre != self.genre:
                self.genre = "MixedGenre"



if __name__ == "__main__":
    # Creating Book objects
    book1 = Book("Harry Potter", 500, "Fantasy")
    book2 = Book("Sherlock Holmes", 300, "Mystery")
    book3 = Book("The Hobbit", 350, "Fantasy")

    print("---- Before Merge ----")
    book1.printDetails()
    book2.printDetails()
    book3.printDetails()

    print("\n---- Merging book2 and book3 into book1 ----")
    book1.merge(book2, book3)

    print("\n---- After Merge ----")
    book1.printDetails()
