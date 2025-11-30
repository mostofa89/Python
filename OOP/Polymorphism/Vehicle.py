class Car:

    def start(self):
        print("Car engine started")


class Bike:

    def start(self):
        print("Bike engine started")


def vehicle_start(v):
    v.start()  # Does not care if v is Car or Bike


c = Car()
b = Bike()
vehicle_start(c)
vehicle_start(b)
