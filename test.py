import unittest
from datetime import date

import workingdays
import workingdays.l10n.it

class TestDefaultLocale(unittest.TestCase):

    def test_is_workingday(self):
        self.assertTrue(workingdays.is_workingday(date(2015, 3, 25)))
        self.assertFalse(workingdays.is_workingday(date(2015, 3, 28)))
        self.assertFalse(workingdays.is_workingday(date(2015, 3, 29)))
        self.assertTrue(workingdays.is_workingday(date(2015, 4, 6)))
        self.assertTrue(workingdays.is_workingday(date(2015, 5, 1)))
      
    def test_add(self):
        self.assertEqual(workingdays.add(date(2015, 3, 25), 2), date(2015, 3, 27))
        self.assertEqual(workingdays.add(date(2015, 3, 25), 3), date(2015, 3, 30))
        self.assertEqual(workingdays.add(date(2015, 3, 25), 4), date(2015, 3, 31))
        self.assertEqual(workingdays.add(date(2015, 3, 28), 1), date(2015, 3, 30))
        
    def test_diff(self):
        self.assertEqual(workingdays.diff(date(2015, 3, 27), date(2015, 3, 25)), 2)
        self.assertEqual(workingdays.diff(date(2015, 3, 28), date(2015, 3, 25)), 2)
        self.assertEqual(workingdays.diff(date(2015, 3, 29), date(2015, 3, 28)), 0)
        
    def test_next(self):
        self.assertEqual(workingdays.next(date(2015, 3, 25)), date(2015, 3, 26))
        self.assertEqual(workingdays.next(date(2015, 3, 27)), date(2015, 3, 30))
        self.assertEqual(workingdays.next(date(2015, 3, 28)), date(2015, 3, 30))

class TestLocaleIt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        workingdays.is_workingday = workingdays.l10n.it.is_workingday

    def test_is_workingday(self):
        self.assertTrue(workingdays.is_workingday(date(2015, 3, 25)))
        self.assertFalse(workingdays.is_workingday(date(2015, 3, 28)))
        self.assertFalse(workingdays.is_workingday(date(2015, 3, 29)))
        self.assertFalse(workingdays.is_workingday(date(2015, 4, 6)))
        self.assertFalse(workingdays.is_workingday(date(2015, 5, 1)))
      
    def test_add(self):
        self.assertEqual(workingdays.add(date(2015, 4, 3), 1), date(2015, 4, 7))
        self.assertEqual(workingdays.add(date(2015, 4, 30), 1), date(2015, 5, 4))
        
    def test_diff(self):
        self.assertEqual(workingdays.diff(date(2015, 5, 4), date(2015, 4, 30)), 1)
        
    def test_next(self):
        self.assertEqual(workingdays.next(date(2015, 4, 3)), date(2015, 4, 7))
        self.assertEqual(workingdays.next(date(2015, 5, 1)), date(2015, 5, 4))
      
if __name__ == '__main__':
    unittest.main()
