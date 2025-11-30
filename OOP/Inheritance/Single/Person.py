class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id


    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}")


print("================================")
print("Single Inheritance Example:")
s = Student("Joy", 22, "CSE123")
s.info()
print("================================")
