# Component classes
class Engine:

    def __init__(self, type, horsepower):
        self.type = type
        self.horsepower = horsepower
    

    def start(self):
        return f"{self.type} engine started with {self.horsepower} HP"
    
    
    def stop(self):
        return "Engine stopped"


class Wheels:

    def __init__(self, count, size):
        self.count = count
        self.size = size
    

    def get_info(self):
        return f"{self.count} wheels of size {self.size} inches"


class MusicSystem:

    def __init__(self, brand):
        self.brand = brand
        self.is_playing = False
    

    def play(self):
        self.is_playing = True
        return f"{self.brand} music system is playing"
    

    def stop(self):
        self.is_playing = False
        return "Music stopped"


# Main class with Has-A relationships
class Car:
    # Car HAS-A Engine
    # Car HAS-A Wheels
    # Car HAS-A MusicSystem
    

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # Composition: Car contains these objects
        self.engine = Engine("V6", 300)
        self.wheels = Wheels(4, 18)
        self.music_system = MusicSystem("Bose")
    

    def start_car(self):
        print(f"\n{self.brand} {self.model} is starting...")
        print(self.engine.start())
        print(self.wheels.get_info())
    

    def play_music(self):
        print(self.music_system.play())
    

    def get_details(self):
        return f"{self.brand} {self.model} - A complete car system"


# Testing
print("=== Has-A Relationship Demo ===")

my_car = Car("Toyota", "Camry")
my_car.start_car()
my_car.play_music()

print(f"\nCar Details: {my_car.get_details()}")
print(f"Engine Type: {my_car.engine.type}")
print(f"Music Brand: {my_car.music_system.brand}")