class Animal:

    def __init__(self, species):
        self.species = species


    def show_species(self):
        print(f"Species: {self.species}")


class Mammal(Animal):

    def __init__(self, species, has_hair=True):
        super().__init__(species)
        self.has_hair = has_hair


    def show_mammal_info(self):
        print(f"Has hair: {self.has_hair}")


class Dog(Mammal):

    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed


    def show_dog_info(self):
        print(f"Breed: {self.breed}")


# Usage
print("Multi-Level Inheritance Example:")
print("=================================")  
dog = Dog("Canine", "Labrador")
dog.show_species()       # from Animal
dog.show_mammal_info()   # from Mammal
dog.show_dog_info()      # from Dog
print("=================================")