from typing import override
class Animal:

    def make_sound(self):
        return "Some generic animal sound"
    

    def sleep(self):
        return "Zzz..."


# Child class 1 - Overrides make_sound()
class Dog(Animal):

    @override
    def make_sound(self):
        return "Woof! Woof!"


# Child class 2 - Overrides make_sound()
class Cat(Animal):

    @override
    def make_sound(self):
        return "Meow!"


# Child class 3 - Overrides make_sound()
class Cow(Animal):

    @override
    def make_sound(self):
        return "Moo!"


# Testing
print("=== Method Overriding Demo ===\n")

# Create objects
generic_animal = Animal()
dog = Dog()
cat = Cat()
cow = Cow()

# Call overridden methods
print(f"Generic Animal: {generic_animal.make_sound()}")
print(f"Dog: {dog.make_sound()}")
print(f"Cat: {cat.make_sound()}")
print(f"Cow: {cow.make_sound()}")

# Inherited method (not overridden)
print(f"\nDog sleeping: {dog.sleep()}")  # Uses parent's method