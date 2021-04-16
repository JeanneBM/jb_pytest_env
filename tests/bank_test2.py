import pytest

class NotEnoughCash(Exception):
    pass


class BankTest2:
    def withdraw_over_amount_test(self):
        with pytest.raises(NotEnoughCash):
            bank = Bank()
            bank.withdraw_money(500)
