# Write a program that simulates a bank system. The program should have classes for accounts, customers,
# and transactions. Accounts should have attributes such as account number, balance, and account 
# type (e.g., checking, savings). Customers should have attributes such as name and contact information.
# Transactions should have attributes such as the account being debited/credited, the amount,
# and the transaction type (e.g., deposit, withdrawal). The program should allow customers to manage
# their accounts, view transaction history, and transfer funds. Use interfaces to implement classes
# for different types of accounts (e.g., individual, joint) and abstract classes for banking operations.
from abc import ABC, abstractmethod
class Accounts(ABC):
    def __init__(self,account_number, balance) -> None:
        self.__account_number = account_number
        self.__balance = balance
    @abstractmethod
    def view_transaction_history(self):
        ...
    @abstractmethod
    def deposit(self):
        ... 
    @abstractmethod
    def withdrawal(self,amount):
        ...
class Individual(Accounts):
    def __init__(self, account_number, balance) -> None:
        super().__init__(account_number, balance)
        self.__transactions = []
        self.__balance = balance
        self.__account_type = "Individual account"

    def withdrawal(self, amount) -> None:
        self.amount = amount
        if self.__balance < self.amount:
            print("You don't have enough money")
        else:
            self.__balance -= self.amount
            self.__transactions.append(f"-{self.amount}")
            print(f"You withdrawed {self.amount} form your {self.__account_type}.")
    def deposit(self, amount: float) -> None:
        self.amount = amount
        self.__balance += self.amount
        self.__transactions.append(f"+{self.amount}")
        print(f"{self.amount}$ is added to balance of {self.__account_type}.")
    def view_transaction_history(self):
        print()
        print("This is your transaction history:")
        for item in self.__transactions:
            print(item)
        print(f"Now the account balance is {self.__balance}$")
class Joint(Accounts):
    def __init__(self, account_number, balance) -> None:
        super().__init__(account_number, balance)
        self.jointowners = []
        self.__balance = balance
        self.__transactions = []
        self.__account_type = "Joint account"

    def withdrawal(self, amount) -> None:
        self.amount = amount
        if self.__balance < self.amount:
            print("You don't have enough money")
        else:
            self.__balance -= self.amount
            self.__transactions.append(f"-{self.amount}")
            print(f"You withdrawed {self.amount} form your {self.__account_type}.")
    def deposit(self, amount: float) -> None:
        self.amount = amount
        self.__balance += self.amount
        self.__transactions.append(f"+{self.amount}")
        print(f"{self.amount}$ is added to balance of {self.__account_type}.")
    def view_transaction_history(self):
        print()
        print("This is your transaction history:")
        for i in self.__transactions:
            print(i)
        print(f"Now the account balance is {self.__balance}")
class Customers:
    def __init__(self, name, contact_details) -> None:
        self.name = name
        self.contact_details = contact_details
        self.__accounts = []
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value == "":
            raise ValueError("name can't be empty...")
        self.__name = value
    @property
    def contact_details(self):
        return self.__contact_details
    @contact_details.setter
    def contact_details(self,value):
        if str(value).startswith('+374'):
            raise ValueError("enter valid contact detail...")
        self.__contact_details = value
    def add_account(self,accunt:Accounts):
        self.__accounts.append(accunt._Accounts__account_number)
    def view_account(self):
        print("Account numbers are:")
        for i in self.__accounts:
            print(i)
class Transaction:
    def __init__(self, db_account:Accounts,amount:int,cr_account:Accounts = None) -> None:
        self.__db_account = db_account
        self.__cr_account = cr_account
        self.__amount = amount
        self.__transaction_type = ('deposit', 'withdrawal')

        

bob = Customers("Bob", +37412345678)
Indacconut = Individual(1570038493,3000)
Indacconut2 = Individual(157007637246,5000)

Indacconut.deposit(4666)
Indacconut.deposit(4200)
Indacconut.withdrawal(2000)
Indacconut.view_transaction_history()
bob.add_account(Indacconut)
bob.add_account(Indacconut2)
bob.view_account()
joint = Joint(157635453,7000)
joint.deposit(4000)



            
    
