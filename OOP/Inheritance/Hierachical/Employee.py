class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def show_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Programmer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language


    def show_programmer(self):
        print(f"{self.name} codes in {self.language}")


class HR(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


    def show_hr(self):
        print(f"{self.name} works in {self.department} department")


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size


    def show_manager(self):
        print(f"{self.name} manages a team of {self.team_size} people")


# Usage
print("Hierarchical Inheritance Example:")
print("----------------------------------")
p = Programmer("Alice", 60000, "Python")
h = HR("Bob", 50000, "Recruitment")
m = Manager("Charlie", 90000, 10)

p.show_employee()
p.show_programmer()
print("----------------------------------")
h.show_employee()
h.show_hr()
print("----------------------------------")
m.show_employee()
m.show_manager()
print("----------------------------------")