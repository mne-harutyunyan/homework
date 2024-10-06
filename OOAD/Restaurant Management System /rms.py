class MenuItem:
    __slots__ = ('__name', '__price', '__ingredients')

    def __init__(self,name,price,ingredients) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value == "":
            raise ValueError("Name can't be empty...")
        self.__name = value
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        if value <= 0:
            raise ValueError("Price must be greater than zero...")
        self.__price = value
    @property
    def ingredients(self):
        return self.__ingredients
    @ingredients.setter
    def ingredients(self,value):
        if value == "":
            raise ValueError("Ingredients can't be empty...")
        self.__ingredients = value
    def __str__(self):
        return f"{self.name} ({self.price} AMD): {self.ingredients}"

class Appetizer(MenuItem):
    __slots__ = ('__calories')

    def __init__(self, name, price, ingredients, calories) -> None:
        super().__init__(name, price, ingredients)
        self.calories = calories
    @property
    def calories(self):
        return self.__calories
    @calories.setter
    def calories(self,value):
        if value <= 0:
            raise ValueError("Calories must be greater than zero...")
        self.__calories = value  

class Entree(MenuItem):
    __slots__ = ('__vegetarian')

    def __init__(self, name, price, ingredients, vegetarian) -> None:
        super().__init__(name, price, ingredients)
        self.vegetarian = vegetarian
    @property
    def vegetarian(self):
        return self.__vegetarian
    @vegetarian.setter
    def vegetarian(self,value):
        if not isinstance(value, bool):
            raise ValueError('Must be "True" or "False"...')
        self.__vegetarian = value 

class Dessert(MenuItem):
    __slots__ = ("__sugar_content")

    def __init__(self, name, price, ingredients,sugar_content) -> None:
        super().__init__(name, price, ingredients)
        self.sugar_content = sugar_content
    @property
    def sugar_content(self):
        return self.__sugar_content
    @sugar_content.setter
    def sugar_content(self,value):
        if value < 0:
            raise ValueError("Sugar content can't be negative... ")
        self.__sugar_content = value 

class Customer:
    __slots__ = ('__name', '__contact_info', '__order_history')

    def __init__(self, name, contact_info) -> None:
        self.name = name
        self.contact_info = contact_info
        self.order_history = []
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value == "":
            raise ValueError("name can't be empty...")
        self.__name = value
    @property
    def contact_info(self):
        return self.__contact_info
    @contact_info.setter
    def contact_info(self,value):
        if not str(value).startswith("+374"):
            raise ValueError("Contact info shuld be valid (e.g.+37412345678)...")
        self.__contact_info = value
    @property
    def order_history(self):
        return self.__order_history
    @order_history.setter
    def order_history(self,value):
        if value == "":
            raise ValueError("Value can't be empty...")
        self.__order_history = value
    def place_order(self, order: 'Order'):
        if not isinstance(order, Order):
            raise ValueError("Invalid order type...")
        self.order_history.append(order)

    def view_order_history(self):
        if not self.order_history:
            print("There are no orders yet...")
        else:
            for i, order in enumerate(self.order_history, 1):
                print(f"Order {i}: {order}")

from abc import ABC, abstractmethod
class Order(ABC):
    __slots__ = ('__customer', '__menu_items', '__total_price')
    
    def __init__(self, customer:'Customer', menu_items = None) -> None:
        self.customer = customer
        self.menu_items = []
        self.total_price = 0
        self.calculate_total_price()

    @property
    def customer(self):
        return self.__customer
    @customer.setter
    def customer(self,value):
        if value == "":
            raise ValueError("Customer can't be empty...")
        self.__customer = value
    @property
    def menu_items(self):
        return self.__menu_items
    @menu_items.setter
    def menu_items(self,value):
        self.__menu_items = value
    @property
    def total_price(self):
        return self.__total_price
    @total_price.setter
    def total_price(self,value):
        self.__total_price = value
    
    @abstractmethod
    def order_type(self):
        pass

    def add_menu_item(self, item: 'MenuItem'):
        if not isinstance(item, MenuItem):
            raise ValueError("Must be a MenuItem...")
        self.__menu_items.append(item)
        self.calculate_total_price()

    def calculate_total_price(self):
        self.__total_price = sum(item.price for item in self.__menu_items)
    
    def __str__(self):
        items_details = ",\n".join((str(item) for item in self.__menu_items))
        return f"Order for {self.customer.name}: {items_details}."

class DineInOrder(Order):
    __slots__ = tuple()
    def order_type(self):
        return "Dine-In order"

class TakeawayOrder(Order):
    __slots__ = tuple()
    def order_type(self):
        return "Takeaway order"

class DeliveryOrder(Order):
    __slots__ = ("__delivery_address")

    def __init__(self, customer: Customer, delivery_address, menu_items=None) -> None:
        super().__init__(customer, menu_items)
        self.delivery_address = delivery_address
    @property
    def delivery_address(self):
        return self.__delivery_address
    @delivery_address.setter
    def delivery_address(self,value):
        if value == "":
            raise ValueError("Delivery address can't be empty...")
        self.__delivery_address = value
    def order_type(self):
        return "Delivery order"

class Review:
    __slots__ =('__customer_name', '__order', '__rating', '__comments')

    def __init__(self,customer_name,order,rating, comments) -> None:
        self.customer_name = customer_name
        self.order = order
        self.rating = rating
        self.comments = comments
    @property
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self,value):
        if value == "":
            raise ValueError("Name can't be empty...")
        self.__customer_name = value
    @property
    def order(self):
        return self.__order
    @order.setter
    def order(self, value):
        if not isinstance(value, Order):
            raise ValueError("Order must be a valid Order...")
        self.__order = value
    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, value):
        if value < 0 or value > 5:
            raise ValueError("Rating must be between 1 and 5...")
        self.__rating = value
    @property
    def comments(self):
        return self.__comments
    @comments.setter
    def comments(self, value):
        if not isinstance(value, str):
            raise ValueError("Comments must be a string...")
        self.__comments = value
    def __str__(self):
        return f"{self.customer_name}'s review: Rating {self.rating}/5 - {self.comments}"
    
appetizer = Appetizer("pizza", 4000, "chesse, tomato, ketchup", 200)
entree = Entree("vegetarian salad", 2500, "tomato, cucumber, peper", True)
dessert = Dessert("Chessecake", 3000, "flour, chesse, chocolate, sugar", 25)

customer = Customer("Bob", "+37412345678")
customer2 = Customer("James", "+37498765432")
dine_in_order = DineInOrder(customer)
dine_in_order.add_menu_item(appetizer)
dine_in_order.add_menu_item(entree)


delivery_order = DeliveryOrder(customer2,"Armenia,Yerevan")
delivery_order.add_menu_item(dessert)
customer.place_order(dine_in_order)
customer2.place_order(delivery_order)
review = Review(customer.name, dine_in_order, 4.5, "So delicious...")
print(review)
review2 = Review(customer2.name,delivery_order, 5 ,"Very fast delivery...")
print(review2)
customer.view_order_history()
print(f"{customer.name} should must pay {dine_in_order.total_price} AMD for {dine_in_order.order_type()}.")
customer2.view_order_history()
print(f"{customer2.name} should must pay {delivery_order.total_price} AMD for {delivery_order.order_type()}.")

