from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


    @abstractmethod
    def show_details(self):
        pass


class Programmer(Employee):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary


    def calculate_salary(self):
        return self.base_salary + 5000  # bonus


    def show_details(self):
        print(f"Programmer: {self.name}, Salary: {self.calculate_salary()}")


class HR(Employee):

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary


    def calculate_salary(self):
        return self.base_salary + 3000  # bonus


    def show_details(self):
        print(f"HR: {self.name}, Salary: {self.calculate_salary()}")


# Driver code
employees = [Programmer("Alice", 50000), HR("Bob", 40000)]

for emp in employees:
    emp.show_details()
