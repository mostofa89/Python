class NikeBangladesh:
    total_stock = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    branch =[]
    sold = 0
    def __init__(self, outlet):
        self.outlet = outlet
        self.stock = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
        NikeBangladesh.branch.append(self.outlet)


    @classmethod
    def status(cls):
        print(f"""Nike Bangladesh Status:
Branches Opened: {NikeBangladesh.branch}
Currently Stocked
{NikeBangladesh.total_stock}
Sold: {NikeBangladesh.sold}""")


    def details(self):
        print(f"""Nike {self.outlet}:
Products Currently Stocked:
{self.stock}
Sold: {NikeBangladesh.sold }""")


    def restockProducts(self, new_stock):
        for shoe, quantity in new_stock.items():
            self.stock[shoe] += quantity
            NikeBangladesh.total_stock[shoe] += quantity


    def productSold(self, sold):
        for shoe, quantity in sold.items():
            if shoe in NikeBangladesh.total_stock:
                NikeBangladesh.total_stock[shoe] -= quantity
                NikeBangladesh.sold += quantity




print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts({"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts({"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()