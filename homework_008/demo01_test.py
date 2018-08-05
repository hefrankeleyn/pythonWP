import unittest
from demo01 import City_Country

class CityCountryTestCase(unittest.TestCase):
    def test_show_city_country(self):
        demo_city_country=City_Country('beijing','haidian')
        city_country=demo_city_country.show_city_and_country()
        self.assertEqual(city_country,'Beijing,Haidian - population 0')
# Test the demo01 class
unittest.main()
