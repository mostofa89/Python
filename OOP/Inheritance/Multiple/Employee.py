# ===========================================================
# Base Employee Class
# ===========================================================
class Employee:
    employee_count = 0
    programmer = 0
    hr = 0

    def __init__(self, name, joining_date, work_experience=0, weekly_work_hour=40):
        self.name = name
        self.joining_date = joining_date
        self.work_experience = work_experience
        self.weekly_work_hour = weekly_work_hour
        Employee.employee_count += 1


    @classmethod
    def showDetails(cls):
        print(f"""Company Workforce Summary:
Total Employee(s): {Employee.employee_count}
Total Programmer(s): {Employee.programmer}
Total HR(s): {Employee.hr}""")


# ===========================================================
# Programmer Class
# ===========================================================
class Programmer(Employee):
    programmer_id_count = 1
    Employee.programmer += 1

    def __init__(self, name, joining_date, work_experience=0, weekly_work_hour=40):
        self.id = f"P-EMP-{Programmer.programmer_id_count}"
        Programmer.programmer_id_count += 1

        self.salary = 0
        self.designation = "Software Engineer"

        super().__init__(name, joining_date, work_experience, weekly_work_hour)

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
        if self.weekly_work_hour > 40:
            extra_hours = self.weekly_work_hour - 40
            self.salary += extra_hours * 200


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

    def __init__(self, name, joining_date, work_experience=0, weekly_work_hour=40):
        self.id = "HR-" + joining_date.replace("-", "")
        super().__init__(name, joining_date, work_experience, weekly_work_hour)


    def showHREmployeeDetails(self):
        print(f"""HR Employee:
Name: {self.name}
ID: {self.id}
Joining Date: {self.joining_date}""")


# ===========================================================
# Intern Programmer Class (Base Intern)
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
        Employee.employee_count += 1
        return Programmer(self.name, self.joining_date, 0, 40)


# ===========================================================
# Multiple Inheritance: Intern + Employee
# ===========================================================
class InternProgrammerEmployee(InternProgrammer, Employee):

    def __init__(self, name, joining_date, intern_type="Unpaid", work_experience=0, weekly_work_hour=40):
        InternProgrammer.__init__(self, name, joining_date, intern_type)
        Employee.__init__(self, name, joining_date, work_experience, weekly_work_hour)
        Employee.programmer += 1


    def promoteToFullProgrammer(self):
        print(f"{self.name} has been promoted to Full Programmer!")
        return Programmer(self.name, self.joining_date, self.work_experience, self.weekly_work_hour)


# ===========================================================
# Driver Code
# ===========================================================
print("=== Employee Management System ===")
print("Initial Employee Details:")
Employee.showDetails()
richard = Programmer("Richard Hendricks", "2021-06-08", 4, 48)
richard.calculateSalary()
richard.showProgrammerDetails()
richard.calculateOvertime()
richard.showProgrammerDetails()
print("====================================")
monica = HR("Monica Hall", "2022-07-06", 2, 40)
monica.showHREmployeeDetails()
print("====================================")
Employee.showDetails()
print("====================================")
gilfoyle = Programmer("Bertram Gilfoyle", "2020-03-02", 6, 35)
gilfoyle.calculateSalary()
gilfoyle.calculateOvertime()
gilfoyle.showProgrammerDetails()
print("====================================")
gavin = Programmer("Gavin Belson", "2016-12-20", 9)
gavin.calculateSalary()
gavin.calculateOvertime()
gavin.showProgrammerDetails()
print("====================================")
yang = InternProgrammerEmployee("Jian Yang", "2023-01-01")
yang.showInternDetails()
promoted_yang = yang.promoteToFullProgrammer()
promoted_yang.calculateSalary()
promoted_yang.showProgrammerDetails()
print("====================================")
jared = InternProgrammerEmployee("Jared Dunn", "2023-06-05", "Paid")
jared.showInternDetails()
promoted_jared = jared.promoteToFullProgrammer()
promoted_jared.calculateSalary()
promoted_jared.showProgrammerDetails()
print("====================================")
Employee.showDetails()
print("====================================")