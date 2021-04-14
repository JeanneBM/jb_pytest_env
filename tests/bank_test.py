class bank_test:
    def test_create_bank(self):
        bank_test1 = bank()
        assert bank_test1.amount == 0
        assert isinstance(bank_test1, bank)

    def add_money_test(self):
        # given
        bank_test1 = bank()

        # when
        bank_test1.add_money(100)

        # then
        assert bank_test1.amount == 100

    def add_money_twice_test(self):
        # given
        bank_test1 = bank()

        # when
        bank_test1.add_money(100)
        bank_test1.add_money(100)

        # then
        assert bank_test1.amount == 200

    def withdraw_money_test(self):
        # given
        bank_test1 = bank()
        bank_test1.add_money(100)

        # when
        money = bank_test1.withdraw_money(100)

        # then
        assert money == 100
        assert bank_test1.amount == 0
