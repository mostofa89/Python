class Passenger:
    count = 0
    
    def __init__(self, name):
        self.name = name
        self.cost = 450
        Passenger.count += 1
        self.bag_weight = 0



    def set_bag_weight(self, weight):
        self.bag_weight = weight
        if  weight > 20:
            self.cost += 50


    def printDetail(self):
        print(f"""Name: {self.name}
Bus Fare: {self.cost} taka""")


print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)