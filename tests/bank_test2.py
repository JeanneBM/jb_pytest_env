import pytest

class NotEnoughCash(Exception):
    pass


class BankTest2:
    def withdraw_over_amount_test(self):
        with pytest.raises(NotEnoughCash):
            bank_test2 = Bank2()
            bank_test2.withdraw_money(500)
