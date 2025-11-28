class  Triangle:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height
        self.__area = 1/2*height*base


    def area(self):
        return self.__area


    def setBase(self, new_base):
        self.__base = new_base


    def getBase(self):
        return self.__base


    def setHeight(self, new_height):
        self.__height = new_height


    def getHeight(self):
        return self.__height



print("====================================")
t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())
print("====================================")
t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())
print("====================================")