class Vehicle:
    
    def __init__(self, brand, **kwargs):
        self.brand = brand


    def show_vehicle_info(self):
        print(f"Brand: {self.brand}")


class Car(Vehicle):
    def __init__(self, doors, **kwargs):
        super().__init__(**kwargs)
        self.doors = doors


    def show_car_info(self):
        print(f"{self.brand} Car has {self.doors} doors")


class ElectricVehicle(Vehicle):

    def __init__(self, battery, **kwargs):
        super().__init__(**kwargs)
        self.battery = battery


    def show_electric_info(self):
        print(f"{self.brand} EV has {self.battery} kWh battery")


class Tesla(Car, ElectricVehicle):

    def __init__(self, brand, doors, battery, autopilot):
        super().__init__(brand=brand, doors=doors, battery=battery)
        self.autopilot = autopilot


    def show_tesla_info(self):
        print(f"Tesla Autopilot Enabled: {self.autopilot}")


# Driver Code
print("========== Hybrid Inheritance Example ==========")
t = Tesla("Tesla", 4, 100, True)

print("\n-- Vehicle Info --")
t.show_vehicle_info()

print("\n-- Car Info --")
t.show_car_info()

print("\n-- Electric Vehicle Info --")
t.show_electric_info()

print("\n-- Tesla Info --")
t.show_tesla_info()
