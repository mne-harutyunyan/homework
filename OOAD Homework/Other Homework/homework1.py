#1. Write a Python class named Person that has attributes for name and age.
#  Include a method to display the person’s details.
#2. Extend the Person class by adding an __init__ constructor method that initializes name and age 
# when an object is created. Ensure the method uses self to assign the values.
#3.Add a method to the Person class called greet that prints a greeting message including the person’s name.
#4.Modify the Person class to make the age attribute private. 
# Provide a method to get the age (get_age) and another method to set the age (set_age) with

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def display(self):
        print(f"My name is {self.name} and I'm {self.__age}.")
    def greeter(self):
        print(f"Hello {self.name}.")
    def get_age(self):
        return self.__age 
    def set_age(self, age):
            if age > 0:  
                self.__age = age
            else:
                raise ValueError("Enter a value age...")
ob=Person("Bob", 1)
ob.display()
ob.greeter()
ob.set_age(6)
ob.display()
ob.set_age(-5)