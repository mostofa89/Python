class Person:

    def __init__(self, name):
        self.name = name


    def show_name(self):
        print(f"Name: {self.name}")


class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


    def show_employee_info(self):
        print(f"Salary: {self.salary}")


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size


    def show_manager_info(self):
        print(f"Manages team of {self.team_size} members")


class Director(Manager):

    def __init__(self, name, salary, team_size, department):
        super().__init__(name, salary, team_size)
        self.department = department


    def show_director_info(self):
        print(f"Director of {self.department} Department")


# Usage
print("Multi-Level Inheritance Example:")
print("=================================")
d = Director("Alice", 200000, 20, "IT")
d.show_name()
d.show_employee_info()
d.show_manager_info()
d.show_director_info()
print("=================================")