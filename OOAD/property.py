# Task 1: Create a class Person that uses the property decorator to control access to the age attribute.
#  Ensure that the age is a positive integer, and if an invalid value is assigned, raise a ValueError.
class Person:
  def __init__(self, age):
    self.age = age

  @property
  def age(self):
    return self.__age
  
  @age.setter
  def age(self, value):
    if not isinstance(value,int) or value < 0 :
      raise ValueError("age must be positive integer")
    self.__age = value

# p = Person(45)
# p.age = -6
# print(p.age)

# Task 2: Implement a class Rectangle where the width and height attributes use the property decorator
#  to calculate the area and perimeter dynamically when accessed.
class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
 
    @property
    def width(self):
       return self.__width
    
    @width.setter
    def width(self,value):
       if value < 0:
          raise ValueError("Width can't be negative...")
       self.__width = value
    
    @property
    def height(self):
       return self.__height
    
    @height.setter
    def height(self,value):
       if value < 0:
          raise ValueError("Height can't be negative...")
       self.__height = value
    @property
    def perimeter(self):
       return 2 * (self.height +  self.width)
    @property
    def area(self):
       return self.height * self.width
    
# example = Rectangle(5,6)
# print(example.area)

# Task 3: Write a class Temperature that stores temperature in Celsius but allows the user to set and get 
# the temperature in Fahrenheit using the property decorator.
class Temperature:
    def __init__(self, CelsiusTemp) -> None:
        self.CelsiusTemp = CelsiusTemp

    @property
    def CelsiusTemp(self):
       return self.__CelsiusTemp
    
    @CelsiusTemp.setter
    def CelsiusTemp(self,value):
       self.__CelsiusTemp = value

    @property
    def Fahrenheit(self):
       return (self.__CelsiusTemp * 9/5) + 32
    
    @Fahrenheit.setter
    def Fahrenheit(self, value):
        self.__CelsiusTemp = (value - 32) * 5/9


# t = Temperature(7) 
# print(t.Fahrenheit)  
# t.Fahrenheit = 78 
# print(t.Fahrenheit)
# print(t.CelsiusTemp) 

# # Task 4: Implement a Descriptor class to manage access to a score attribute in a Student class.
# #  Use the __get__ and __set__ methods to ensure the score is within a valid range (e.g., 0-100).


class Descriptor:
    def __init__(self) -> None:
        self.__score = 0
    def __get__(self, instance, owner):
        return self.__score
    def __set__(self, instance, value):
        if value not in range(0,101):
            raise ValueError("Score must be between 0-100 ")
        self.__score = value
class Student:
    score = Descriptor()


# bob = Student()
# print(bob.score)
# bob.score = 89
# print(bob.score)
# bob.score = 46

# Task 5: Build a class ValidatedString where you implement a custom descriptor that validates if the string
#  has a minimum length when assigned. Demonstrate this descriptor with a class User
#  where the username attribute uses this descriptor.

class ValidatedString:
    def __init__(self) -> None:
        self.__string = ""

    def __get__(self, instance, owner):
        return self.__string
    
    def __set__(self, instance, value):
        if len(value) < 8:
            raise ValueError("String must contain 8 character... ")
        self.__string = value

class User:
    username = ValidatedString()

# bob = User()
# bob.username = "bob9895t"
# print(bob.username)
# bob.username = "bob14564"

# Task 6: Create a class Employee that manages the salary attribute with a custom descriptor.
#  Ensure that the __get__ and __set__ methods validate the salary (e.g., it must be positive 
# and not exceed a predefined maximum).

class ValidatedSalary:
   
    def __get__(self,instance, owner):
        return instance.__salary
    def __set__(self,instance, value):
        if value < 0 or value > 1000000:
            raise ValueError("Value must be between 0 to 1000000...")
        instance.__salary = value

class Employee:
    def __init__(self,value = 1) -> None:
        self.salary = value
    salary = ValidatedSalary()

# bob = Employee()
# print(bob.salary)
# bob.salary = 199
# print(bob.salary)

# Task 7: Implement a class RangeDescriptor that ensures any value set within the class 
# is within a predefined range (e.g., 1 to 100). Use this descriptor
#  in a class Product to manage the price attribute.

class RangeDescriptor:

    def __get__(self,instance,owner):
        return instance.__price
    def __set__(self,instance,value):
        if value not in range(1,101):
            raise ValueError("Price mus be between 1 to 100...")
        instance.__price = value
class Product:
    def __init__(self, price) -> None:
       self.price = price
    price = RangeDescriptor()

# table = Product(34)
# print(table.price)    
# table.price = 77
# print(table.price)    


# Task 8: Write a class PasswordValidator that uses a descriptor to validate passwords 
# according to a set of rules (e.g., minimum length, contains numbers). 
# Show how this is used in a class Account.

class PasswordValidator:
    def __get__(self, instance, owner):
        return instance.__password
    def __set__(self, instance, value):
        if not True in (x.isdigit() for x in value) or not True in (x.isalpha() for x in value):
            raise ValueError("Password must contain at least one number and one letter...")
        if len(value) < 8:
            raise ValueError("Password must contain at least 8 character...")
        instance.__password = value
class Account:

    def __init__(self, password="Example1"):
        if password is not None:
            self.password = password
    password = PasswordValidator()

hello = Account()
hello.password = "hello87879"
print(hello.password)

