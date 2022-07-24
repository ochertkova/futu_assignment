import unittest

from utils import format_date

class TestDate(unittest.TestCase):
    def test_empty(self):
        testcase = ""
        expected = None
        self.assertEqual(format_date(testcase),expected)

    def test_str(self):
        testcase = "AAAA"
        expected = None
        self.assertEqual(format_date(testcase),expected)

    def test_basic(self):
        testcase = "2022-02-13T21:24:30Z"
        expected = "13/02/2022"
        self.assertEqual(format_date(testcase),expected)

    def test_given_format(self):
        testcase = "2022-07-24T21:24:30Z"
        expected = "24.07.2022"
        self.assertEqual(format_date(testcase, '%d.%m.%Y'),expected)


if __name__ == "__main__":
    unittest.main()