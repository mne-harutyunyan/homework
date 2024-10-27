import abc
from datetime import datetime
from typing import Optional
from account import Account
class TransactionManager(abc.ABC):
    @abc.abstractmethod
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        ...
    @abc.abstractmethod
    def show_transaction_history(self) -> None:
        ...

class Transaction:
    def __init__(self,  from_account: 'Account', to_account: Optional['Account'], amount: float, transaction_type: str) -> None:
        self.__from_account = from_account
        self.__to_account = to_account
        self.__amount = amount
        self.__transaction_type = transaction_type
        self.__timestamp = datetime.now()
    def log(self) -> None:
        print(f"Your {self.__amount}$ {self.__transaction_type} transaction has been executed from {self.__from_account.get_account_type()} to {self.__to_account.get_account_type()} account in {self.__timestamp}.")