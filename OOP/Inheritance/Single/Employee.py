class Employee:
    employee_count = 0
    programmer = 0
    hr = 0

    def __init__(self, name, joining_date, work_experience=0, weekly_work_hour=None):
        self.name = name
        self.joining_date = joining_date
        self.work_experience = work_experience
        self.weekly_work_hour = weekly_work_hour
        Employee.employee_count += 1


    @classmethod
    def showDetails(cls):
        print(f"""Company workforce:
Total Employee(s): {Employee.employee_count}
Total Programmer Employee(s): {Employee.programmer}
Total HR Employee(s): {Employee.hr}""")


# ===========================================================
# Programmer Class
# ===========================================================
class Programmer(Employee):
    programmer_id_count = 1
    Employee.programmer += 1

    def __init__(self, name, joining_date, work_experience=0, weekly_work_hour=None):
        # Auto ID
        self.id = f"P-EMP-{Programmer.programmer_id_count}"
        Programmer.programmer_id_count += 1

        # Default values
        self.salary = 0
        self.designation = "Software Engineer"

        # Call parent constructor
        Employee.__init__(self, name, joining_date, work_experience, weekly_work_hour)

        # Assign designation
        if work_experience < 3:
            self.designation = "Junior Software Engineer"
        elif work_experience < 5:
            self.designation = "Software Engineer"
        elif work_experience < 8:
            self.designation = "Senior Software Engineer"
        else:
            self.designation = "Technical Lead"


    def calculateSalary(self):
        base = 30000
        increment = self.work_experience * 5000
        self.salary = base + increment


    def calculateOvertime(self):
        if self.weekly_work_hour and self.weekly_work_hour > 40:
            extra = self.weekly_work_hour - 40
            overtime_pay = extra * 200
            self.salary += overtime_pay


    def showProgrammerDetails(self):
        print(f"""Programmer Employee:
Name: {self.name}
ID: {self.id}
Joining Date: {self.joining_date}
Designation: {self.designation}
Salary: BDT {self.salary}""")


# ===========================================================
# HR Class
# ===========================================================
class HR(Employee):
    Employee.hr += 1

    def __init__(self, name, joining_date, work_experience=0, weekly_work_hour=None):
        self.id = "HR-" + joining_date.replace("-", "")
        Employee.__init__(self, name, joining_date, work_experience, weekly_work_hour)


    def showHREmployeeDeatails(self):
        print(f"""HR Employee:
Name: {self.name}
ID: {self.id}
Joining Date: {self.joining_date}""")


# ===========================================================
# Intern Programmer  (NO inheritance)
# ===========================================================
class InternProgrammer:
    intern_id_count = 1

    def __init__(self, name, joining_date, intern_type="Unpaid"):
        self.name = name
        self.joining_date = joining_date
        self.intern_type = intern_type
        self.id = f"INT-{InternProgrammer.intern_id_count}"
        InternProgrammer.intern_id_count += 1


    def showInternDetails(self):
        print(f"""Intern Programmer:
Name: {self.name}
ID: {self.id}
Joining Date: {self.joining_date}
Intern Type: {self.intern_type}""")


    def promoteToProgrammer(self):
        print(f"{self.name} has been promoted to Programmer!")
        Employee.programmer += 1
        Employee.employee_count += 1  # new employee

        return Programmer(self.name, self.joining_date, 0, 40)



# ===========================================================
# Driver Code
# ===========================================================

Employee.showDetails()
print("=========1=========")

richard = Programmer("Richard Hendricks", "2021-06-08", 4, 48)
richard.calculateSalary()
print("=========2=========")
richard.showProgrammerDetails()
print("=========3=========")
richard.calculateOvertime()
print("=========4=========")
richard.showProgrammerDetails()

print("=========5=========")
monica = HR("Monica Hall", "2022-07-06", 2, 40)

print("=========6=========")
monica.showHREmployeeDeatails()

print("=========7=========")
Employee.showDetails()

print("=========8=========")
gilfoyle = Programmer("Bertram Gilfoyle", "2020-03-02", 6, 35)
gilfoyle.calculateSalary()
print("=========9=========")
gilfoyle.calculateOvertime()
print("=========10=========")
gilfoyle.showProgrammerDetails()

print("=========11=========")
gavin = Programmer("Gavin Belson", "2016-12-20", 9)
gavin.calculateSalary()
gavin.calculateOvertime()
gavin.showProgrammerDetails()

print("=========12=========")
yang = InternProgrammer("Jian Yang", "2023-01-01")
yang.showInternDetails()

print("=========13=========")
jared = InternProgrammer("Jared Dunn", "2023-06-05", "Paid")
jared.showInternDetails()

print("=========14=========")
jared = jared.promoteToProgrammer()

print("=========15=========")
Employee.showDetails()

print("=========16=========")
yang = yang.promoteToProgrammer()
yang.calculateSalary()
yang.showProgrammerDetails()

print("=========17=========")
Employee.showDetails()
