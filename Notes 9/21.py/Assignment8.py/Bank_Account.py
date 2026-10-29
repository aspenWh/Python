
import random


class Bank_Account:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.00

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False