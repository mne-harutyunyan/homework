# SOLID principles
# Dependency Inversion Principle

# bad example
class BadBudgetReport:
    def __init__(self,database:'MyBadSQLDatabase') -> None:
        self.database = database
    def open(self,date):
        print(f"Opening database in {date}")
    def save(self,data):
        print(f"Saving {data} to database")

class MyBadSQLDatabase:
    def insert(self,data):
        print(f"Inserting {data} into MySQL database...")
    def update(self,data):
        print(f"Updating {data} in MySQL database..")
    def delete(self,data):
        print(f"Deleting {data} from MySQL database...")

# db = MyBadSQLDatabase()
# budgetreport = BadBudgetReport(db)
# budgetreport.open("12/10/2024")
# budgetreport.save("Semester report")

# good example

from abc import ABC, abstractmethod

class GoodBudgetReport:
    def __init__(self,database:'Database') -> None:
        self.database = database
    def open(self,date):
        print(f"Opening database in {date}")
    def save(self,data):
        print(f"Saving {data} to database")
        self.database.update(data)
class Database(ABC):
    @abstractmethod
    def insert(self):
        ...
    @abstractmethod
    def update(self):
        ...
    @abstractmethod
    def delete(self):
        ...

class MyGoodSQL(Database):
    def insert(self,data):
        print(f"Inserting {data} into MySQL database...")
    def update(self,data):
        print(f"Updating {data} in MySQL database..")
    def delete(self,data):
        print(f"Deleting {data} from MySQL database...")
class MyMongoDB(Database):
    def insert(self,data):
        print(f"Inserting {data} into MyMongo database...")
    def update(self,data):
        print(f"Updating {data} in Myongo database..")
    def delete(self,data):
        print(f"Deleting {data} from MyMongo database...")

db = MyMongoDB() 
report = GoodBudgetReport(db)
report.open("12/10/2024")
report.save("Annual Budget")