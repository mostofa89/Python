class Shape:

    def area(self, width, height):
        return width * height


class Color:

    def __init__(self, color):
        self.color = color


    def show_color(self):
        print(f"Color: {self.color}")


# Multiple inheritance
class Rectangle(Shape, Color):

    def __init__(self, color):
        Color.__init__(self, color)


# Usage
print("Multiple Inheritance Example:")
print("==============================")
rect = Rectangle("Blue")
print("Area:", rect.area(5, 10))
rect.show_color()
print("==============================")