class BracuStudent:
    def __init__(self,  name, home):
        self.__name = name
        self.home = home
        self.__passStatus = False


    def getName(self):
        return self.__name


    def get_passStatus(self):
        return self.__passStatus


    def get_pass(self):
        self.__passStatus = True


    def show_details(self):
        print(f"""Student Name: {self.__name}
Lives in {self.home}
Have Bus Pass? {self.__passStatus} """)



class BracuBus:
    def __init__(self, destination, capacity = 2):
        self.__destination = destination
        self.__passenger = []
        self.__capacity = capacity


    def show_details(self):
        print(f"""Bus Route: {self.__destination}
Passengers Count: {len(self.__passenger)} (Max: {self.__capacity})
Passengers On Board: {self.__passenger}""")


    def board(self, *students):
        if len(students) != 0:
            for student in students:
                if len(self.__passenger) < self.__capacity:
                    if student.get_passStatus() == True:
                        if student.home == self.__destination:
                            self.__passenger.append(student.getName())
                            print(f"{student.getName()} boarded the bus.")

                        else:
                            print(f"You got on the wrong bus!")

                    else:
                        print("You don't have a bus pass!")

                else:
                    print("Bus is full!")


        else:
            print("No Paasenger.")







st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()