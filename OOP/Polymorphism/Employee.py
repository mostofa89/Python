class Employee:
    
    def work(self):
        print("Employee working...")


class Programmer(Employee):

    def work(self):
        print("Programmer coding...")


class Manager(Employee):

    def work(self):
        print("Manager managing...")


employees = [Employee(), Programmer(), Manager()]
for e in employees:
    e.work()
