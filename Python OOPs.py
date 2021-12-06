# Task 1 

class BankAccount:
    def __init__(self):
        self.balance=0
    def check_balance(self):
        print("Your current balance is: ", self.balance)
    def deposit(self, depositAmount):
        self.balance = self.balance+depositAmount
        print("Money has been successsfully deposited, and your current balance is: ", self.balance)
    def withdraw(self, withdrawAmount):
        if self.balance>withdrawAmount:
            self.balance = self.balance-withdrawAmount
        else:
            print("The balance is insufficient")
            
obj1 = BankAccount()                   
obj1.check_balance()


obj1.deposit(2000)
obj1.check_balance()


obj1.withdraw(400)
obj1.check_balance()


obj1.withdraw(1600)
obj1.check_balance()




# Task 2

class MinimumBalanceAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)
        self.minbal = 5000
    def withdraw(self, amount):
        if self.balance-amount<self.minbal:
            print("Sorry, you can't withdraw the amount you want to, some amount of minimum balance has to be maintained in your Bank Account")
        else:
            BankAccount.withdraw(self, amount)



obj2 = MinimumBalanceAccount()


obj2.deposit(10000)


obj2.withdraw(9000)

obj2.withdraw(4500)
obj2.check_balance()

