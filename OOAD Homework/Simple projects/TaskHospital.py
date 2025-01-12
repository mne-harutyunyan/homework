# Write a program that simulates a hospital management system. The program should have classes for patients,
# doctors, and medical staff. Patients should have attributes such as name, age, and medical history.
# Doctors should have attributes such as name and contact information. Medical staff should have attributes 
# such as name and position. The program should allow doctors to manage patient information and appointments,
# and medical staff to manage hospital operations. Use inheritance to implement classes for different types
# of medical procedures (e.g., surgeries, check-ups) and abstract classes for medical operations.

from abc import ABC, abstractmethod
class Person:
    def __init__(self,name) -> None:
        self.name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == " ":
            raise ValueError("Name can't be empty...")
        self.__name = value

class Patient(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name)
        self.age = age
        self.__appointments = {}
        self.medical_history = []
    @property
    def age(self):                              
        return self.__age
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Age can't be negative...")
        self.__age = value 
    @property
    def appointments(self):                              
        return self.__appointments
    @appointments.setter
    def appointments(self, value):
        if value  == " ":
            raise ValueError("appointments can't be empty...")
        self.__appointments = value 
class Doctors(Person):
    def __init__(self, name, contact_information) -> None:
        super().__init__(name)
        self.contact_information = contact_information
        self.__appointments = {}
    @property
    def contact_information(self):
        return self.__contact_information
    @contact_information.setter
    def contact_information(self, value):
        if not str(value).startswith("374"):
            raise ValueError("Enter valid contact information(e.g. +374xxxxxxxx). ")
        self.__contact_information = value
    def manage_patient_information(self, patient : Patient):
        print(f"{self.name} is managing {patient.name} information.")
    def make_appointment(self, patient: Patient, date):
        if isinstance(patient, Patient):
            if not(date in self.__appointments.keys()) and not (date in patient.appointments.keys()): 
                self.__appointments[date] = patient.name
                patient.appointments[date] = self.name
                print(f"{self.name} made an appointment for {patient.name} in {date}.")
    def cancel_appointment(self, patient: Patient, date):
        if isinstance(patient, Patient):
            if date in self.__appointments.keys() and date in patient.appointments.keys(): 
                self.__appointments.pop(date)
                patient.appointments.pop(date)
                print(f"{self.name} cancelled an appointment for {patient.name} in {date}.")
class Medical_staff:
    def __init__(self,name,position) -> None:
        self.name = name
        self.position = position
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == " ":
            raise ValueError("Name can't be empty...")
        self.__name = value
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if value == " ":
            raise ValueError("Position can't be empty...")
        self.__position = value
    def managing_medical_operations(self, medical_procedures : 'MedicalProcedures'):
        print(f"{self.name} is managing {medical_procedures.medical_procedures_type()}.")

class MedicalProcedures(ABC):
    @abstractmethod
    def medical_procedures_type(self):
        ...
class Surgeries(MedicalProcedures):
    def medical_procedures_type(self):
        return "Surgery"
class Check_Ups(MedicalProcedures):
    def medical_procedures_type(self):
        return "Check-up"

doctor1 = Doctors("Dr. Hasmik", 37456789876)
patient1 = Patient("Bob", 56)
doctor1.make_appointment(patient1, "October 28")
surgery = Surgeries()
nurse = Medical_staff("Jane","Nurse")
nurse.managing_medical_operations(surgery)
doctor1.cancel_appointment(patient1,"October 28")