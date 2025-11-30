# Component classes
class Address:
    
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
    

    def get_full_address(self):
        return f"{self.street}, {self.city}, {self.state} - {self.zipcode}"


class Course:

    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits
    

    def get_info(self):
        return f"{self.code}: {self.name} ({self.credits} credits)"


class ContactInfo:

    def __init__(self, email, phone):
        self.email = email
        self.phone = phone
    

    def get_contact(self):
        return f"Email: {self.email}, Phone: {self.phone}"


# Main class with Has-A relationships
class Student:
    # Student HAS-A Address
    # Student HAS-A ContactInfo
    # Student HAS-A list of Courses
    

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.address = None  # Will be set later
        self.contact = None
        self.courses = []  # List of Course objects
    

    def set_address(self, street, city, state, zipcode):
        self.address = Address(street, city, state, zipcode)
    

    def set_contact(self, email, phone):
        self.contact = ContactInfo(email, phone)
    

    def enroll_course(self, course):
        self.courses.append(course)
    

    def display_info(self):
        print(f"\n{'='*50}")
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        
        if self.address:
            print(f"Address: {self.address.get_full_address()}")
        
        if self.contact:
            print(f"Contact: {self.contact.get_contact()}")
        
        if self.courses:
            print("\nEnrolled Courses:")
            for course in self.courses:
                print(f"  - {course.get_info()}")
        
        print('='*50)


# Testing
print("=== Student Has-A Relationship Demo ===")

# Create student
student = Student("John Smith", "ST12345")

# Set address (Student HAS-A Address)
student.set_address("123 Main St", "Boston", "MA", "02101")

# Set contact (Student HAS-A ContactInfo)
student.set_contact("john.smith@email.com", "555-1234")

# Enroll courses (Student HAS-A Courses)
student.enroll_course(Course("Data Structures", "CS201", 3))
student.enroll_course(Course("Database Systems", "CS301", 4))
student.enroll_course(Course("Web Development", "CS250", 3))

# Display all information
student.display_info()