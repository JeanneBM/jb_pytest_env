class Bank2:
    def __init__(self):
        self.amount = 0

    def add_money(self, money: int):
        self.amount += money

    def withdraw_money(self, money):
        if money > self.amount:
            raise NotEnoughCash('Nie ma tyle')

        self.amount -= money

        return money
