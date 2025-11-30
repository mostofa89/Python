class Animal:

    def __init__(self, species):
        self.species = species


class Dog(Animal):

    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed


    def show(self):
        print(f"Species: {self.species}, Breed: {self.breed}")


print("================================")
print("Single Inheritance Example:")
dog = Dog("Mammal", "German Shepherd")
dog.show()
print("================================")
