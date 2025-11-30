class Student:
    total_student = 0
    bracu_student = 0
    others_student = 0

    def __init__(self, name, dept, university = "BRAC University"):
        self.name = name
        self.dept = dept
        self.university = university
        Student.total_student += 1
        if university == "BRAC University":
            Student.bracu_student += 1

        else:
            Student.others_student += 1


    @classmethod
    def printDetails(clss):
        print(f"""Total Student(s): {Student.total_student}
BRAC University Student(s): {Student.bracu_student}
Other Institution Student(s): {Student.others_student}""")


    def individualDetail(self):
        print(f"""Name: {self.name}
Department: {self.dept}
Institution: {self.university}""")


    @classmethod
    def createStudent(cls, name, dept, university = "BRAC University"):
        new_Student = cls (name, dept, university)
        return new_Student




Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()