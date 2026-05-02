# OOPs with Encapsulation

class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def get_balance(self):
        return self.__balance


# Object
acc = BankAccount("Suresh", 1000)

acc.deposit(500)
print("Balance:", acc.get_balance())