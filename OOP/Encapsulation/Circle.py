import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__vloume = 4/3*math.pi*radius**3


    def getRadius(self):
        return self.__radius


    def volume(self):
        return self.__vloume


print("====================================")
c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" , c1.volume())
print("====================================")
c2 = Circle(5)
print("Second circle radius:" , c2.getRadius())
print("Second circle area:" , c2.volume())
print("====================================")