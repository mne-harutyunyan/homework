# Write a program that simulates a university course management system. The program should have classes for
# courses, students, and professors. Courses should have attributes such as name, instructor, and content.
# Students should have attributes such as name and contact information. Professors should have attributes such as
# name and contact information. The program should allow professors to create and manage courses, and students
# to enroll in courses, complete assignments, and view their progress. Use interfaces to implement classes
# for different types of courses (e.g., undergraduate, graduate) and abstract classes for course assignments.

from abc import ABC, abstractmethod
class Courses(ABC):
    def __init__(self, name, instructor = None, content = None) -> None:
        self.name = name
        self.instructor = instructor
        self.content = content
        self.students = []
    @abstractmethod
    def course_type(self):
        ...
class Undergraduate(Courses):
    def __init__(self, name, instructor = None, content = None) -> None:
        super().__init__(name, instructor, content)
    def course_type(self):
        print("This is Undergraduate course...")
class Graduate(Courses):
    def __init__(self, name, instructor = None, content = None) -> None:
        super().__init__(name, instructor, content)
    def course_type(self):
        print("This is Graduate course...")

class Person:
    def __init__(self, name, contact_information) -> None:
        self.name = name
        self.contact_information = contact_information
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == " ":
            raise ValueError("Name can't be empty...")
        self.__name = value
    @property
    def contact_information(self):
        return self.__contact_information
    @contact_information.setter
    def contact_information(self, value):
        if not str(value).startswith("374"):
            raise ValueError("Enter valid contact information(e.g. +374xxxxxxxx). ")
        self.__contact_information = value

class Students(Person):
    def __init__(self, name, contact_information) -> None:
        super().__init__(name, contact_information)
        self.__courses = []
        self.__assignments = []
        self.__completed_assignments = []
        self.__assignments_history = []
    def enroll_course(self,course: Courses):
        if isinstance(course, Courses):
            self.__courses.append(course.name)
            course.students.append(self.name)
            print(f"{self.name} enrolled {course.name} course .")
    def view_courses(self):
        if len(self.__courses) == 1:
            print(f"{self.name}'s enrolled course is ")
        else:
            print(f"{self.name}'s enrolled courses are ")
        for i in self.__courses:
            print("~",i)
    def complete_assignment(self, assignment_name):
        if assignment_name in self.__assignments:
            self.__completed_assignments.append(assignment_name)
            self.__assignments.remove(assignment_name)
            print(f"{self.name} completed {assignment_name} ...")
    def view_progress(self):
        for i in self.__assignments_history:
            print("~", i)
    def get_courses(self):
        return self.__courses
    def get_assignments(self):
        return self.__assignments
class Proffessors(Person):
    def __init__(self, name, contact_information) -> None:
        super().__init__(name, contact_information)
        self.__courses = [] 
    def view_courses(self):
        if len(self.__courses) == 1:
            print(f"{self.name}'s course is ")
        else:
            print(f"{self.name}'s courses are ")
        for i in self.__courses:
            print("~",i)
    def create_course(self, course : Courses, content):
        if isinstance(course, Courses):
            self.__courses.append(course.name)
            course.instructor = self.name
            course.content = content
    def delete(self,course : Courses):
        if isinstance(course, Courses):
            self.__courses.remove(course.name)
    def give_assignments(self, course: Courses , student : Students, assignment_name):
        if course.name in student.get_courses():
            student.get_assignments().append(assignment_name)
            print(f"{self.name} gives {assignment_name} assignment to {student.name}.")


proffessor1 = Proffessors("Jack", 37412233267)
student1 = Students("Bob", 37456773322)
course1 = Undergraduate("Math")
course2 = Graduate("History")

proffessor1.create_course(course1,"Even numbers")
proffessor1.create_course(course2,"Tigran the Great")
proffessor1.view_courses()
student1.enroll_course(course1)
proffessor1.give_assignments(course1,student1,"Task1")
proffessor1.give_assignments(course1,student1,"Task2")

student1.complete_assignment("Task1")
student1.complete_assignment("Task2")
student1.view_progress()
student1.view_courses()



