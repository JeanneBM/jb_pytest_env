class Sort_test:
  
    @pytest.fixture
    def names(self):
        return ['Asia', 'Kasia', 'Marysia']

    def sort_test(self, names):
        # when
        sorted_names = sort_by(names, first_letter=True)

        # then
        assert sorted_names == ['Asia', 'Kasia', 'Marysia']

    def reverse_sort_test(self, names):
        # when
        sorted_names = sort_by(names, last_letter=True)

        assert sorted_names == ['Asia', 'Kasia', 'Marysia']

    def by_length_test(self, names):
        # when
        sorted_names = sort_by(names, length=True)

        assert sorted_names == ['Asia', 'Kasia', 'Marysia']
