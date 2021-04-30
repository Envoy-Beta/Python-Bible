class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit (self, amount):
        self.balance += amount # --> self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: £{}".format(self.balance))

class Checking(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    #Name of object without all the extra text
    def __str__(self):
        return "{}'s Checking Account Balance: £{}".format(self.name, self.balance)

x = Checking("Zayid", 500)
print(x)

x.deposit(300)
x.statement()

x.withdraw(1000)
x.statement()

x.withdraw(800)
x.statement()
x.withdraw(1)

class Savings(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

        #Name of object without all the extra text
    def __str__(self):
        return "{}'s Savings Account Balance: £{}".format(self.name, self.balance)

Z = Checking("Zayid", 500)
T = Savings("Tazmine", 700)

print(Z)
print(T)

T.withdraw(700)
T.statement()
T.withdraw(1)