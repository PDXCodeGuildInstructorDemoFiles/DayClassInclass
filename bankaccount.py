class BankAccount:
    def __init__(self, balance, acc_name):
        self.balance = balance
        self.acc_name = acc_name

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print('Thank you {}. Your remaining balance is ${}.'.format(self.acc_name, self.balance))
        else:
            print('Sorry, you have no money!')

    def deposit(self, amount):
        self.balance += amount
        print('Thank you {}. Your remaining balance is ${}.'.format(self.acc_name, self.balance))

    def __str__(self):
        return 'Hello {}, your balance is ${}.'.format(self.acc_name, self.balance)


class BankAccountSpecial(BankAccount):
    def __init__(self, balance, acc_name):
        super().__init__(balance, acc_name)

    def withdraw(self, amount):
        if self.balance - amount >= 100:
            self.balance -= amount
            print('Thank you {}. Your remaining balance is ${}.'.format(self.acc_name, self.balance))
        elif 100 > self.balance - amount >= 0:
            print('Your account would be under the min')
        else:
            print('Sorry, you have no money!')


if __name__ == "__main__":
    print('this some tesing stuff.')
