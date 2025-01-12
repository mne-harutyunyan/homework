# SOLID principles
# Single Responsibility Principle
#bad example
class BadEmployeeCls:
    def __init__(self,name) -> None:
        self.__name = name
    
    def GetName(self):
        return self.__name
    def printTimeSheetReport(self):
        print(f"This is {self.__name}'s Time Sheet Report...")

e = BadEmployeeCls("Bob")
e.printTimeSheetReport()

#good example
class GoodEmployeeCls:
    def __init__(self,name) -> None:
        self.name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value == '':
            raise ValueError("Name can't be empty...")
        self.__name = value
class TimeSheetReport:
    def __init__(self, employee: 'GoodEmployeeCls') -> None:
        self.employee = employee
    @property
    def employee(self):
        return self.__employee
    @employee.setter
    def employee(self,value):
        if not isinstance(value, GoodEmployeeCls):
            raise ValueError("Employee must be Good Employee...")
        self.__employee = value
    def PrintTimeSheetReport(self):
        print(f"This is Good employee - {self.employee.name}'s Time Sheet Report...")

g = GoodEmployeeCls("Jack")
report = TimeSheetReport(g)
report.PrintTimeSheetReport()