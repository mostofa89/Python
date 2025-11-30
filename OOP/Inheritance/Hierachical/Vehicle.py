class Vehicle:

    def __init__(self, brand):
        self.brand = brand


    def show_brand(self):
        print(f"Brand: {self.brand}")


class Car(Vehicle):

    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def show_car(self):
        print(f"{self.brand} Car has {self.doors} doors")


class Bike(Vehicle):

    def __init__(self, brand, type_bike):
        super().__init__(brand)
        self.type_bike = type_bike


    def show_bike(self):
    
        print(f"{self.brand} Bike type: {self.type_bike}")

class Truck(Vehicle):

    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity


    def show_truck(self):
        print(f"{self.brand} Truck capacity: {self.capacity} tons")


# Usage
print("Hierarchical Inheritance Example:")
print("----------------------------------")
c = Car("Toyota", 4)
b = Bike("Yamaha", "Sport")
t = Truck("Volvo", 20)
print("----------------------------------")
c.show_brand(); c.show_car()
print("----------------------------------")
b.show_brand(); b.show_bike()
print("----------------------------------")
t.show_brand(); t.show_truck()
print("----------------------------------")
