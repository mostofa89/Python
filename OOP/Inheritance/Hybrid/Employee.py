class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary

    def show_employee_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")


class Programmer(Employee):
    def __init__(self, language, **kwargs):
        super().__init__(**kwargs)
        self.language = language

    def show_programmer_info(self):
        print(f"{self.name} codes in {self.language}")


class HR(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

    def show_hr_info(self):
        print(f"{self.name} works in {self.department} department")


class Manager(Programmer, HR):
    def __init__(self, name, salary, language, department, team_size):
        super().__init__(name=name, salary=salary, language=language, department=department)
        self.team_size = team_size

    def show_manager_info(self):
        print(f"{self.name} leads a team of {self.team_size} people in {self.department}")


# Driver Code
print("========== Hybrid Inheritance Example ==========")
m = Manager("Alice", 150000, "Python", "IT", 5)

print("\n-- Employee Info --")
m.show_employee_info()

print("\n-- Programmer Info --")
m.show_programmer_info()

print("\n-- HR Info --")
m.show_hr_info()

print("\n-- Manager Info --")
m.show_manager_info()
print("===============================================")


