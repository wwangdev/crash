import unittest
from city_functions import print_city_country


class PrintCityTest(unittest.TestCase):
    def test_print_city_country(self):
        city = "dalian"
        country = "china"
        self.assertEqual(print_city_country(city, country), 'Dalian, China')


    def test_print_city_country_popultion(self):
        city = "dalian"
        country = "china"
        population = 40000
        self.assertEqual(print_city_country(city, country, population), 'Dalian, China')


if __name__ == '__main__':
    unittest.main()
