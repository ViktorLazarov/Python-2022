class BankAccount:
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        return self.balance

    def withdraw(self,withdraw_amount):
        self.balance -= withdraw_amount
        return self.balance

acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
acct.deposit(10)
acct.withdraw(3)
print(acct.balance)
