import unittest
from demo02 import Employee

class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.employee=Employee('xiaoming','ming',2000)
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary,7000)
    def test_give_custom_raise(self):
        self.employee.give_raise(2000)
        self.assertEqual(self.employee.annual_salary,4000)

unittest.main()
