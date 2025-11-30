class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def show_info(self):
        print(f"Doctor: {self.name} ({self.specialization})")


class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def show_appointments(self):
        print(f"Patient: {self.name}")
        for a in self.appointments:
            print(f"- {a.doctor.name} on {a.date}")
        print("====================================")


class Appointment:
    def __init__(self, doctor, patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date


# Driver code
d1 = Doctor("Dr. Karim", "Cardiologist")
p1 = Patient("Joy", 22)

a1 = Appointment(d1, p1, "5 Dec 2025")
p1.add_appointment(a1)

p1.show_appointments()
d1.show_info()
