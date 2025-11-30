class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def show_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Programmer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language


    def show_programmer_info(self):
        print(f"Programming Language: {self.language}")


class SeniorProgrammer(Programmer):

    def __init__(self, name, salary, language, team_size):
        super().__init__(name, salary, language)
        self.team_size = team_size


    def show_senior_info(self):
        print(f"Leads a team of {self.team_size} members")


# Usage
print("Multi-Level Inheritance Example:")
print("=================================")
senior = SeniorProgrammer("Alice", 120000, "Python", 5)
senior.show_employee_info()
senior.show_programmer_info()
senior.show_senior_info()
print("=================================")