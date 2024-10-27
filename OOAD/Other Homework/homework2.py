# 1. Design a class Employee with private attributes employee_id, name, and salary. 
#    Provide methods to set and get these values. Ensure that salary cannot be negative.
class Employee:
    def __init__(self,employee_id:int, name:str, salary:int) -> None:
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary
    def setValue(self, setId, setName, setSalary):
        self.__employee_id = setId
        self.__name = setName
        if setSalary > 0:
            self.__salary = setSalary
        else:
            raise ValueError("salary can't be negative...")
    def getValue(self):
        return f"Employee ID : {self.__employee_id},\nName : {self.__name},\nSalary : {self.__salary}."

# Bob=Employee(789896,"Bob",500000)
# print(Bob.getValue())
# Bob.setValue(566767,"Bobby",1000000)
# print(Bob.getValue())

# try:
#     Bob.setValue(566767,"Bobby",-1)
# except ValueError:
#     print("Error ka")

# Bob.setValue(566767,"Bobby",-1)


# 2. Design a class Book with private attributes title, author, and price. 
#    Create methods to set and get the values of these attributes.
#    Ensure that the price cannot be set below a certain value (e.g., 10).

class Book:
    def __init__(self,title:str, author:str, price:int) -> None:
        self.__title = title
        self.__author = author
        self.__price = price
    def setValue(self, setTitle, setAuthor, setPrice):
        self.__title = setTitle
        self.__author = setAuthor
        if setPrice > 10:
            self.__price = setPrice
        else:
            raise ValueError("Price can't be lower than 10AMD..")
    def getValue(self):
        return f"Title : {self.__title},\nAuthor : {self.__author},\nPrice : {self.__price} AMD."

# TheLittlePrince = Book("The Little Prince","Antoine de Saint-Exupéry","5000")
# print(TheLittlePrince.getValue())
# TheLittlePrince.setValue("Metamorphosis","Franz Kafka", 8000)
# print(TheLittlePrince.getValue())
# TheLittlePrince.setValue("Metamorphosis","Franz Kafka", 8)


# 3. Create a class Student with private attributes name, roll_number, and grades. 
#    Implement methods to add grades, calculate the average grade, and display the student’s information.
#    Ensure that the grades are between 0 and 100.

class Student:
    def __init__(self, name, roll_number,*grades)->None:
        self.__name = name
        self.__roll_number = roll_number
        self.__grades = grades
    def setGrades(self,*setGrades):
        for i in setGrades:
            if i in range(0,100):
                self.__grades += (i,)
            else:
                raise ValueError("Grades must be between 0 and 100...")
    def averageGrade(self):
            return f"The average grade is : {sum(self.__grades)/len(self.__grades)}"

    def display(self):
        print(f"Name : {self.__name},\nRoll number : {self.__roll_number},\nGrades : {self.__grades}.")

# Bob=Student("Bob", 1000, 68,56,78)
# Bob.setGrades(78,90,54,8)
# Bob.display()
# print(Bob.averageGrade())
# Bob.setGrades(78,90,101,8)



# 4. Design a class ShoppingCart that encapsulates a private list of items (items).
#    Implement methods to add an item, remove an item, and display the total number of items in the cart.
#    Each item should have a name and price.

class ShoppingCard:
    def __init__(self,items) -> None:
        self.__items = []
    def addItem(self,name, price):
        self.__items.append({"name":name,"price":price})
    def removeItem(self,item):
        for i in self.__items:
            if i["name"] == item:
                self.__items.remove(i)
    def display(self):
        return f"The total number of items in the cart is {len(self.__items)}."
    
# food = ShoppingCard("food")
# food.addItem("bread",250)
# food.addItem("butter",650)
# food.addItem("ice cream", 300)
# print(food.display())
# food.removeItem("bread")
# print(food.display())


# 5. Design a class Product with private attributes product_id, product_name, and quantity_in_stock.
#    Implement methods to set and get the values of these attributes 
#    and to adjust the quantity_in_stock (e.g., adding stock or reducing stock).

class Product:
    def __init__(self,product_id:int, product_name:str, quantity_in_stock:float) -> None:
        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock

    def getProductID(self):
        return self.__product_id
    def getProductName(self):
        return self.__product_name
    def getQuantityInStock(self):
        return self.__quantity_in_stock
    
    def setProductID(self,newProductId):
        self.__product_id = newProductId
    def setProductName(self, newProductName):
        self.__product_name = newProductName
    def setQuantityInStock(self,newQuantityInStock):
        if newQuantityInStock > 0:
            self.__quantity_in_stock = newQuantityInStock
        else:
            raise ValueError("Stock quantity can't be negative...")
        
    def adjust_stock(self, amount):
        if self.__quantity_in_stock - amount >= 0:
            self.__quantity_in_stock -= amount
        else:
            print("Can't be reduced anymore.")

chair = Product(789896,"chair",5)
print(chair.getProductName())
print(chair.getProductID())
print(chair.getQuantityInStock())

chair.setProductName("table")
print(chair.getProductName())
chair.setQuantityInStock(9)
print(chair.getQuantityInStock())
chair.adjust_stock(6)
print(chair.getQuantityInStock())
chair.adjust_stock(6)


