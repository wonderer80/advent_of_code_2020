import unittest
from day1 import Day1

class Day1Test(unittest.TestCase):

    def test_expense_report(self):
        d = Day1('day1_input1.txt')
        sum_value = 2020
        expected_result = 514579
        result = d.expense_report(sum_value)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
