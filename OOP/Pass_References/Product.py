class Product:
    def __init__(self, name, stock, category="General"):
        self.name = name
        self.stock = stock
        self.category = category


    def printDetails(self):
        print(f"{self.name} -> Stock: {self.stock}, Category: {self.category}")


    def combine(self, *products):
        for p in products:
            self.stock += p.stock
            if p.category != self.category:
                self.category = "MixedCategory"


if __name__ == "__main__":
    # Creating Product objects
    p1 = Product("Laptop", 50, "Electronics")
    p2 = Product("Mouse", 150, "Electronics")
    p3 = Product("Notebook", 200, "Stationery")

    print("---- Before Combine ----")
    p1.printDetails()
    p2.printDetails()
    p3.printDetails()

    print("\n---- Combining p2 and p3 into p1 ----")
    p1.combine(p2, p3)

    print("\n---- After Combine ----")
    p1.printDetails()
