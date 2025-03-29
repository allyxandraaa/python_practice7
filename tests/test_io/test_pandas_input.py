import unittest
from app.io.input import pandas_input


class TestPandasInput(unittest.TestCase):

    def test_pandas_input_1(self):
        expected_output = (
            "   id     name  age  score\n"
            "0   1    Alice   28   95.5\n"
            "1   2      Bob   32   88.0\n"
            "2   3  Charlie   24   76.5\n"
            "3   4    Diana   45   92.3"
        )
        self.assertEqual(
            pandas_input(
                "test_data/test_pandas_input_data/test_pandas_input_data_1.csv"
            ),
            expected_output,
        )

    def test_pandas_input_2(self):
        expected_output = (
            "    id   product  price  quantity\n"
            "0  101  Widget A  19.99        50\n"
            "1  102  Widget B  24.99        35\n"
            "2  103  Widget C  14.50       100\n"
            "3  104  Widget D  29.99        25\n"
            "4  105  Widget E   9.99       200"
        )
        self.assertEqual(
            pandas_input(
                "test_data/test_pandas_input_data/test_pandas_input_data_2.csv"
            ),
            expected_output,
        )

    def test_pandas_input_3(self):
        expected_output = (
            "    timestamp          value   flag\n"
            "0  1640995200   1.234568e+08   True\n"
            "1  1641081600   9.876543e+08  False\n"
            "2  1641168000  1.797693e+308   True\n"
            "3  1641254400 -1.797693e+308  False\n"
            "4  1641340800   1.000000e-15   True"
        )
        self.assertEqual(
            pandas_input(
                "test_data/test_pandas_input_data/test_pandas_input_data_3.csv"
            ),
            expected_output,
        )
