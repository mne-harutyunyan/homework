# SOLID principles
# Open/Closed Principle

# bad example
class BadOrderCls:
    def __init__(self, weight, shipping) -> None:
        self.__weight = weight
        self.__shipping = shipping
    def GetShppingType(self):
        return self.__shipping
    def GetShippingCost(self):
        if self.__shipping == "byair":
            return f"By air bad shipping cost is {self.__weight * 5}$."
        elif self.__shipping == "byground":
            return f"By ground bad shipping cost is {self.__weight * 2}$."
# o = BadOrderCls(3,"byair")
# print(o.GetShippingCost())
# b = BadOrderCls(4, "byground")
# print(b.GetShippingCost())

# good example 
class GoodOrderCls:
    def __init__(self, weight) -> None:
        self.weight = weight
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self,value):
        if value < 0:
            raise ValueError("Weight can't be negative...")
        self.__weight = value

from abc import ABC, abstractmethod

class Shipping(ABC):
    @abstractmethod
    def GetCost(self, order: 'GoodOrderCls'):
        ...
    @abstractmethod
    def GetType(self, order: 'GoodOrderCls'):
        ...

class Ground(Shipping):
    def __init__(self,order: 'GoodOrderCls') -> None:
        self.__order = order
    def GetCost(self):
        return f"Good shipping cost by ground is {self.__order.weight * 2}$."
    def GetType(self):
        return self.__name__

class Air(Shipping):
    def __init__(self,order: 'GoodOrderCls') -> None:
        self.__order = order
    def GetCost(self):
        return f"Good shipping cost by air is {self.__order.weight * 5}$."
    def GetType(self):
        return self.__name__

order1 = GoodOrderCls(3)
cost = Air(order1)
print(cost.GetCost())
order1 = GoodOrderCls(3)
cost = Ground(order1)
print(cost.GetCost())