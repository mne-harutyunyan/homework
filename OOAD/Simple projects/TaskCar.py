from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def get_model(self):
        return self.__model

    def get_make(self):
        return self.__make

    def get_price(self):
        return self.__price

class Electric(Car):
    def __init__(self, make, model, price, battery_usage_in_hour):
        super().__init__(make, model, price)
        self.__battery_usage_in_hour = battery_usage_in_hour

    def drive(self):
        print(f"{self.get_make()} {self.get_model()} is driving...")

    def stop(self):
        print(f"{self.get_make()} {self.get_model()} stops...")

class Hybrid(Car):
    def __init__(self, make, model, price, oil_usage_in_hour):
        super().__init__(make, model, price)
        self.__oil_usage_in_hour = oil_usage_in_hour

    def drive(self):
        print(f"{self.get_make()} {self.get_model()} is driving...")

    def stop(self):
        print(f"{self.get_make()} {self.get_model()} stops...")

class Customers:
    def __init__(self, name, contact_details) -> None:
        self.name = name
        self.contact_details = contact_details
        self.cars = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name can't be empty.")
        self.__name = value

    @property
    def contact_details(self):
        return self.__contact_details

    @contact_details.setter
    def contact_details(self, value):
        if not str(value).startswith('+374'):
            raise ValueError("Enter valid contact detail.")
        self.__contact_details = value

    def search(self, car: Car, salespeople: 'SalesPeople'):
        if car.get_model() in salespeople.cars_for_sale:
            print(f"Yes, {salespeople.name} has {car.get_make()} {car.get_model()}.")
            return True
        else:
            print(f"There is no such car.")
            return False

    def purchase(self, car: Car, salespeople: 'SalesPeople'):
        if self.search(car, salespeople):
            salespeople.remove_car(car)
            print(f" {self.name} bought {car.get_make()} {car.get_model()}.")
        else:
            print(f"there is no such car")
    def view_cars(self):
        for i in self.cars:
            print(i)

class SalesPeople:
    def __init__(self, name, commission_rate=1) -> None:
        self.name = name
        self.commission_rate = commission_rate
        self.cars_for_sale = {}
        self.sales_history = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name can't be empty.")
        self.__name = value

    @property
    def commission_rate(self):
        return self.__commission_rate

    @commission_rate.setter
    def commission_rate(self, value):
        if value <= 0:
            raise ValueError("Commission rate can't be negative.")
        self.__commission_rate = value

    def add_car(self, car: Car):
        self.cars_for_sale[car.get_model()] = car
        self.sales_history.append(f"Added car: {car.get_make()} {car.get_model()}.")

    def remove_car(self, car: Car):
        if car.get_model() in self.cars_for_sale:
            removed_car = self.cars_for_sale.pop(car.get_model())
            self.sales_history.append(f"Sold car: {removed_car.get_make()} {removed_car.get_model()}.")
        else:
            print(f"There is no such car")

bmw = Electric('BMW', "X6", 50000, 7)
toyota = Hybrid('Toyota', "Camry", 30000, 5)

salesperson = SalesPeople("Bob")
salesperson.add_car(bmw)
salesperson.add_car(toyota)

customer = Customers("Jack", "+37412345678")
customer.search(bmw, salesperson) 
customer.purchase(bmw, salesperson)
