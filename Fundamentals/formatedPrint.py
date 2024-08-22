name = "Jhon Smith"
age = 21
prof = "Student"
salary = 112.6533333

# Using F-String
print(f"Name : {name}, Age : {age}, Proffession : {prof}, Salary : {salary}.")


# Multiline Print and formated number
print(f"""Name : {name}.
Age : {age}.
Proffession : {prof}.
Salary : {salary : .2f}""")

#next line and tab
print("Name : " + str(name) + "\nAge : " + str(age))
print("Name : " + str(name) + "\tAge : " + str(age))