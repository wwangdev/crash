import unittest
from employee import Emplyoee as em

class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.base = 10000
        self.custom_raise = 50000
        self.my_employee = em('ww', self.base)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, self.base + 5000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(self.custom_raise)
        self.assertEqual(self.my_employee.salary, self.base + self.custom_raise)


if __name__ == '__main__':
    unittest.main()