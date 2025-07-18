class BankAccount:

    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def deposite(self, money):
        if money > 0:
            self.balance += money
            print(f'Вы успешно пополнили счет. На вашем счете: {self.balance}')

    def withdraw(self, money):
        if money > self.balance:
            print(f'недостаточно средств на счете')
        elif money < self.balance:
            self.balance -= money
            print(f'Вы успешно сняли {money}, остаток на Вашем счете {self.balance}')

    def all_balaces(self):
        print(f'Ваш баланс {self.balance}')

man = BankAccount('123456', 700)

man.all_balaces()
man.deposite(100)
man.withdraw(1000)
man.deposite(1200)


