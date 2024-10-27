import abc
class Account(abc.ABC):
    def __init__(self,account_number: int, balance: float, account_type: str) -> None:
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
    @abc.abstractmethod
    def deposit(self, amount: float) -> None:
        ...
    @abc.abstractmethod
    def withdraw(self, amount: float) -> None:
        ...
    @abc.abstractmethod
    def transfer(self, destination: 'Account', amount: float) -> None:
        ...
    @abc.abstractmethod
    def show_balance(self) -> None:
        ...
    @abc.abstractmethod
    def get_account_type(self) -> str:
        ...
    
class CheckingAccount(Account):
    def __init__(self,account_number: int, balance: float, overdraft_limit: float):
        super().__init__(account_number,balance, "Checking")
        self.__overdraft_limit = overdraft_limit
    def deposit(self, amount: float) -> None:
        self.amount = amount
        self.balance += self.amount
        print(f"{self.amount}$ is added to balance. Now balance is {self.balance}.")
    def withdraw(self, amount: float) -> None:
        self.amount = amount
        if self.balance + self.__overdraft_limit < self.amount:
            print("You don't have enough money")
        else:
            self.balance -= self.amount
            print(f"You withdrawed {self.amount} form your account. Now your balance is {self.balance}.")
    def transfer(self, destination: 'Account', amount: float) -> None:
        self.amount = amount
        if self.balance + self.__overdraft_limit < self.amount:
            print("You don't have enough money")
        else:
            self.withdraw(amount)
            destination.deposit(amount)
    def show_balance(self) -> None:
        print(f"{self.account_type} account balance is {self.balance}$.")    
    def get_account_type(self) -> str:
        return self.account_type

class SavingsAccount(Account):
    def __init__(self,account_number: int, balance: float, interest_rate: float):
        super().__init__(account_number, balance, "Saving")
        self.__interest_rate = interest_rate
    def deposit(self, amount: float) -> None:
        self.amount = amount
        self.balance += self.amount
        print(f"{self.amount}$ is added to balance. Now balance is {self.balance}.")
    def withdraw(self, amount: float) -> None:
        self.amount = amount
        if self.balance < self.amount:
            print("You don't have enough money")
        else:
            self.balance -= self.amount
            print(f"You withdrawed {self.amount} form your account. Now your balance is {self.balance}.")
    def transfer(self, destination: 'Account', amount: float) -> None:
        self.amount = amount
        if self.balance < self.amount:
            print("You don't have enough money")
        else:
            self.withdraw(amount)
            destination.deposit(amount)
    def show_balance(self) -> None:
        print(f"{self.account_type} account balance is {self.balance}$.")    
    def get_account_type(self) -> str:
        return self.account_type
from typing import List

class JointAccount(Account):
    def __init__(self,account_number: int, balance: float, joint_owners: List[str]):
        super().__init__(account_number, balance, "Joint")
        self.__joint_owners = joint_owners
    def deposit(self, amount: float) -> None:
        self.amount = amount
        self.balance += self.amount
        print(f"{self.amount}$ is added to balance. Now balance is {self.balance}.")
    def withdraw(self, amount: float) -> None:
        self.amount = amount
        if self.balance < self.amount:
            print("You don't have enough money")
        else:
            self.balance -= self.amount
            print(f"You withdrawed {self.amount} form your account. Now your balance is {self.balance}.")
    def transfer(self, destination: 'Account', amount: float) -> None:
        self.amount = amount
        if self.balance < self.amount:
            print("You don't have enough money")
        else:
            self.withdraw(amount)
            destination.deposit(amount)
    def show_balance(self) -> None:
        print(f"{self.account_type} account balance is {self.balance}$.")    
    
    def get_account_type(self) -> str:
        return self.account_type

    def add_owner(self, customer_name: str) -> None:
          self.__joint_owners.append(customer_name)


