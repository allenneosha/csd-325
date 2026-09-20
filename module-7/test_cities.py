import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do city and country names like 'Egypt, Africa' work?"""
        formatted_city_country = city_country('egypt', 'africa')
        self.assertEqual(formatted_city_country, 'Egypt, Africa')

if __name__ == '__main__':
    unittest.main()