class BankAccount():
    def __init__(self,owner,balance=0.0):
        self.owner = owner
        self.balance = balance
    def deposit(self,deposit_amount):
        self.balance += deposit_amount
    def withdraw(self,withdraw_amount):
        self.balance -= withdraw_amount

acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
acct.deposit(10)
acct.withdraw(3)
print(acct.balance)