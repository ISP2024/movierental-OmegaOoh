import unittest
from rental import Rental
from movie import Movie
import pricing


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, ["Action", "Adventure",
                                                        "Drama", "Sci-Fi"])
        self.regular_movie = Movie("Air", 2023, ["Drama", "Sport"])
        self.childrens_movie = Movie("Frozen", 2013, ["Adventure", "Comedy",
                                                      "Fantasy", "Musical",
                                                      "Children"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2023, ["Drama", "Sport"])
        self.assertEqual("Air (2023)", str(m))
        self.assertTrue(m.is_genre("Drama"))
        self.assertTrue(m.is_genre("sPort"))
        self.assertFalse(m.is_genre("action"))

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2)
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_price(), 3.5)
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        rental = Rental(self.regular_movie, 10)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)
