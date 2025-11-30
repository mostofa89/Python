from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


    @abstractmethod
    def perimeter(self):
        pass


# Circle class inherits Shape
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius ** 2


    def perimeter(self):
        return 2 * 3.14 * self.radius


# Rectangle class inherits Shape
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width


    def perimeter(self):
        return 2 * (self.length + self.width)


# Driver code
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area()}, Perimeter: {shape.perimeter()}")
