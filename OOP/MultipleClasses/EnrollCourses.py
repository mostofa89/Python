class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
       
        self.enrollments = []

    def enroll(self, enrollment):
        self.enrollments.append(enrollment)


    def show_courses(self):
        print(f"Student: {self.name}")
        print("Enrolled Courses:")
        for e in self.enrollments:
            print(f"- {e.course.course_name} ({e.semester})")
        print("====================================")


class Course:
    def __init__(self, course_name):
        self.course_name = course_name


class Enrollment:
    def __init__(self, student, course, semester):
        self.student = student
        self.course = course
        self.semester = semester


# Driver Code
s1 = Student("Joy", "22101234")
c1 = Course("Algorithms")
c2 = Course("Database Systems")

e1 = Enrollment(s1, c1, "Fall 2024")
e2 = Enrollment(s1, c2, "Fall 2024")

s1.enroll(e1)
s1.enroll(e2)

s1.show_courses()


