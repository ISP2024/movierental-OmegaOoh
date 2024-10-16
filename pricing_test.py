import unittest
from movie import Movie
from rental import Rental
import pricing

class TestPriceCode(unittest.TestCase):
    def setUp(self):
        self.new_movie = Movie("Mulan", 2024, ["Action", "Adventure", "Drama"])
        self.regular_movie = Movie("CitizenFour", 2014, ["Biography",
                                                         "Documentary"])
        self.childrens_movie = Movie("Frozen", 2013, ["Adventure", "Comedy",
                                                      "Fantasy", "Musical",
                                                      "Children"])
        self.new_child_movie = Movie("Inside Out 2", 2024, ["Choildrens", "Drama"])

    def test_new_movie(self):
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.price_code, pricing.NewPrice())
        rental = Rental(self.new_child_movie, 10)
        self.assertEqual(rental.price_code, pricing.NewPrice())

    def test_children_movie(self):
        rental = Rental(self.childrens_movie, 10)
        self.assertEqual(rental.price_code, pricing.ChildrenPrice())
        rental = Rental(self.new_child_movie, 5)
        self.assertNotEqual(rental.price_code, pricing.ChildrenPrice())
    
    def test_regular_price(self):
        rental = Rental(self.regular_movie, 10)
        self.assertEqual(rental.price_code, pricing.RegularPrice())