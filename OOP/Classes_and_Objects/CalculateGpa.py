class StudentDatabase:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = {}
        self.cgpa = 0.0


    def calculateGPA(self, *items):
        result, semistar=items
        couses_tuple=()
        courses = 0
        gpa_sum = 0
        self.grades[semistar] = {}

        for it in result:
            k, v = it.split(":")
            key = k.strip()
            val = v.strip()
            value = float(val.strip())
            couses_tuple += key,
            gpa_sum += value*3
            courses += 1
            self.cgpa = gpa_sum/(courses*3)

        self.grades[semistar][couses_tuple]='{:.2f}'.format(self.cgpa)
        gpa_sum = 0


    def printDetails(self):
        print(f"Name: {self.name}\nID: {self.id}")
        for key, value in self.grades.items():
            print(f"Courses taken in {key}:")
            for courses, result in value.items():
                for course in courses:
                    print(course)
                    print(f"GPA: {result}")



s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()