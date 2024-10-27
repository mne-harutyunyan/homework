from  typing import List
from account import Account

class Customer:
    def __init__(self, name: str, contact_info: str) -> None:
        self.__name = name
        self.__contact_info = contact_info
        self.__accounts = []
   

    def add_account(self, account: Account) -> None:
        self.__accounts.append(account)
        print(f"Added {account.get_account_type()} Account to {self.__name}'s profile.")
    
    def view_accounts(self) -> None:
        print(f"{self.__name} has {len(tuple(x for x in self.__accounts))} accounts: ")
        for account in self.__accounts:
            account.show_balance()
    
    def view_transaction_history(self) -> None:
        pass

