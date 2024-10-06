class Person:
    __slots__ = ("__name", "__age", "__email")
    def __init__(self,name,age,email) -> None:
        self.name = name
        self.age = age
        self.email = email
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value == "":
            raise ValueError("name can't be empty...")
        self.__name = value
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if value <= 0:
            raise ValueError("age can't be negative...")
        self.__age = value
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,value):
        if "@" not in value or len(value) < 2:
            raise ValueError("enter valid email...")
        self.__email = value
# p = Person("Bob", 45, "mane@list.ru")
# print(p.__slots__)
# p.phone_number = 37477674653

