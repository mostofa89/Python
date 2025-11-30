class Farmer:
    def __init__(self, id=None, name=None):
        self.crops = []
        self.fishes = []
        self.id = id
        self.name = name

        if id == None:
            print("Welcome to your farm!")

        elif id == None and name != None:
            print(f"Welcome to your farm, {self.name}!")

        else:
            print(f"Welcome to your farm. Your farm ID is {self.id}!")

    def addCrops(self, *crops):
        for crop in crops:
            if crop not in self.crops:
                self.crops.append(crop)

            if len(self.crops) == 0:
                print("No crop added.")

            else:
                print(f"{len(self.crops)} crop(s) added.")

    def addFishes(self, *fishes):
        for fish in fishes:
            if fish not in self.fishes:
                self.fishes.append(fish)

            if len(self.fishes) == 0:
                print("No fish added.")
            else:
                print(f"{len(self.fishes)} fish(s) added.")


    def showGoods(self):
        crops_str = ", ".join(self.crops)
        fishes_str = ", ".join(self.fishes)
        if len(self.crops) == 0:
            print(f"You don't have any crop(s).")

        else:
            print(f"You have {len(self.crops)} crop(s):")
            print(crops_str)

        if len(self.fishes) == 0:
            print(f"You don't have any fish(s).")

        else:
            print(f"You have {len(self.fishes)} fish(s):")
            print(fishes_str)


f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes("Pangash", "Magur")
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")