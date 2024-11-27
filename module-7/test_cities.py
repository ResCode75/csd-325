# Rachel Shaw - 7.1 Assignment - 11/26/2024
import unittest
from  city_functions import city_country

#create testcase
class test (unittest.TestCase):
    #function for testing 
    def test_city_country(self):
        formatted = city_country(city = "Tokyo", country = "Japan")
        self.assertEqual(formatted, "Tokyo, Japan.")

unittest.main()