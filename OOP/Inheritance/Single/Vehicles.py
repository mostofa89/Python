class Vehicle:

    def __init__(self, wheels):
        self.wheels = wheels


class Car(Vehicle):

    def __init__(self, wheels, model):
        super().__init__(wheels)
        self.model = model


    def details(self):
        print(f"Model: {self.model}, Wheels: {self.wheels}")


print("================================")
print("Single Inheritance Example:")
c = Car(4, "Toyota Corolla")
c.details()
print("================================")