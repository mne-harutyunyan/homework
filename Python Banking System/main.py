from account import CheckingAccount, SavingsAccount, JointAccount
from transfer import Transaction
from customer import Customer

if __name__ == "__main__":
    customer = Customer("Bob", "bob@example.com")
    checking_acc = CheckingAccount(1570065635344400, 50000, 2000)
    savings_acc = SavingsAccount(1570065635344499, 50788, 298)
    joint_acc = JointAccount(1570087676543800, 67800, 78)
    customer.add_account(checking_acc)
    customer.add_account(savings_acc)
    customer.add_account(joint_acc)
    customer.view_accounts()
    Transaction(checking_acc,savings_acc,10000,"deposit", 10).log()

    