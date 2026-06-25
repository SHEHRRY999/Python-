class Account:
    def __init__(self, balance, accNum):
        self.balance = balance
        self.accNum = accNum
    def credit(self, amount):
        self.balance = self.balance + amount

    def debit(self, amount):
        self.balance = self.balance - amount
    
    def printBalance(self):
        print(self.balance)

acc1 = Account(324990, 342)
acc1.credit(2300)
acc1.debit(44411)
acc1.printBalance()

        