# doing python way of encapsulation (not strict through)
# leaves it to the wisdom of the programmer
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # private attribute

    @property
    def balance(self):          # getter method
        return self.__balance

    def deposit(self, amount):  # setter method
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid balance")

    def withdraw(self, amount):  # method to withdraw money
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

account = BankAccount(1000)
print(account.balance)  # accessing balance through getter

account.deposit(3000)
print(account.balance)  # accessing balance through getter

account.withdraw(2000)
print(account.balance)  # accessing balance through getter
