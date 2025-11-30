class Student:
    id = 0

    def __init__(self, name, dept, age, cgpa):
        self.name = name
        self.age =  age
        self.dept = dept
        self.cgpa = cgpa
        Student.id += 1


    def showDetails(self):
        print(f"""ID: {Student.id}
Name: {self.name}
Department: {self.dept}
Age: {self.age}
CGPA: {self.cgpa}""")


    @classmethod
    def from_String(cls, str1):
        name, dept, age, cgpa = str1.split("-")
        new_student = cls(name, dept, age, cgpa)
        return new_student





s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()