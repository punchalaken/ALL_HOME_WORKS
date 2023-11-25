import unittest
from data_func.data_functions import unique_names, top_3_person, supre_name
import pytest


class TestsUnittest(unittest.TestCase):
    test_lst = [['Евгений', 'Артем', 'Дмитрий'], ['Евгений', 'Артем', 'Олег', 'Дмитрий'],
                ['Евгений', 'Олег', 'Артем', 'Дмитрий']]

    @unittest.skipIf(len(test_lst) == 0, reason='Слишком маленький список')
    def test_unique_names_type(self):
        res = unique_names(self.test_lst)
        self.assertIsInstance(res, str, msg='Возвращаемая строка не соответствует требованиям')

    @unittest.skipIf(len(test_lst) == 0, reason='Слишком маленький список')
    def test_top_3(self):
        res = unique_names(self.test_lst)
        self.assertIsInstance(res, str)


    def test_unique_names_data(self):
        res = unique_names(self.test_lst)
        self.assertFalse(res is None)

    @unittest.expectedFailure
    def test_unique_names_nums(self):
        res = unique_names(1, 2, 3, 4, 1, 24, 2)
        self.assertIsInstance(res, str)


class TestsPyTest():


    def test_unique_names(self):
        res = unique_names([['Евгений', 'Артем', 'Дмитрий'], ['Евгений', 'Артем', 'Олег', 'Дмитрий'],
                ['Евгений', 'Олег', 'Артем', 'Дмитрий']])
        assert isinstance(res, str)

    @pytest.mark.xfail
    def test_false(self):
        res = unique_names(1, 2, 35, 12, 452, 23)
        assert res is None

    @pytest.mark.parametrize(
        'lst',
        [
            ([['Евгений', 'Артем', 'Дмитрий'], ['Евгений', 'Артем', 'Олег', 'Дмитрий'],
                ['Евгений', 'Олег', 'Артем', 'Дмитрий']]),
            ([['Олег', 'Наталья', 'Адилет'], ['Адилет', 'Адилет', 'Олег'], ['Адилет', 'Олег', 'Наталья']])
        ]
    )
    def test_unique_names_params(self, lst):
        res = unique_names(lst)
        assert isinstance(res, str)



