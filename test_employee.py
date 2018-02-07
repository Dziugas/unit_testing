import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Dziugas', 'Tornau', 50000)
        self.emp_2 = Employee('Billie', 'Jean', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Dziugas.Tornau@gmail.com')
        self.assertEqual(self.emp_2.email, 'Billie.Jean@gmail.com')

        self.emp_1.first = 'Jimmy'
        self.emp_2.first = 'Bobby'

        self.assertEqual(self.emp_1.email, 'Jimmy.Tornau@gmail.com')
        self.assertEqual(self.emp_2.email, 'Bobby.Jean@gmail.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Dziugas Tornau')
        self.assertEqual(self.emp_2.fullname, 'Billie Jean')

        self.emp_1.first = 'Jimmy'
        self.emp_2.first = 'Bobby'

        self.assertEqual(self.emp_1.fullname, 'Jimmy Tornau')
        self.assertEqual(self.emp_2.fullname, 'Bobby Jean')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 50000*1.05)
        self.assertEqual(self.emp_2.pay, 60000*1.05)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Tornau/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Jean/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
