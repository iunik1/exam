import unittest
from datetime import date
import MainApp as app

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.app = app

    def test_with_my_birth(self):
        date2 = date(2003,6,21)
        self.assertEqual(app.my_function(date2),967)
        
    def test_with_random(self):
        date2 = date(1999,1,12)
        self.assertEqual(app.my_function(date2),1198)
    
    def test_same_date(self):
        date2 = date(2022,1,1)
        self.assertEqual(app.my_function(date2),0)

if __name__ == '__main__':
    unittest.main()