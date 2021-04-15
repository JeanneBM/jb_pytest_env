class Bank:
    def __init__(self):
        self.amount = 0

    def add_money(self, money: int):
        self.amount += money

    def withdraw_money(self, money):
        self.amount -= money

        return money


