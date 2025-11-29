class Employee:
    def __init__(self, salary):
        self.__salary = salary


    @property
    def salary(self):
        return self.__salary


    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary")


# Driver code
print("====================================")
emp1 = Employee(50000)
print("Initial Salary:", emp1.salary)
emp1.salary = 60000
print("Updated Salary:", emp1.salary)
emp1.salary = -1000  # This should trigger the invalid salary message
print("Final Salary:", emp1.salary)
print("====================================")
