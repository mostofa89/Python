import math
from typing import override
# Parent class
class Shape:

    def area(self):
        return 0
    

    def perimeter(self):
        return 0
    

    def description(self):
        return "This is a generic shape"


# Child class 1 - Rectangle
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
    

    @override
    def area(self):
        return self.length * self.width
    

    @override
    def perimeter(self):
        return 2 * (self.length + self.width)
    

    @override
    def description(self):
        return f"Rectangle with length {self.length} and width {self.width}"


# Child class 2 - Circle
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    

    @override
    def area(self):
        return math.pi * self.radius ** 2
    

    @override
    def perimeter(self):
        return 2 * math.pi * self.radius
    

    @override
    def description(self):
     
        return f"Circle with radius {self.radius}"

# Child class 3 - Triangle
class Triangle(Shape):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    

    @override
    def area(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    

    @override
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    

    @override
    def description(self):
        return f"Triangle with sides {self.side1}, {self.side2}, {self.side3}"


# Testing
print("=== Shape Method Overriding Demo ===\n")

shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(shape.description())
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print("-" * 40)