import unittest
from movie import Movie
from movie_catalog import MovieCatalog


class TestMovieCatalog(unittest.TestCase):
    """Test for MovieCatalog Class"""

    def setUp(self) -> None:
        """Test fixture contains

        catalog = a movie catalog
        """
        self.catalog = MovieCatalog()

    def test_singleton(self):
        """There is only one MovieCatalog Object."""
        catalog1 = MovieCatalog()
        catalog2 = MovieCatalog()
        self.assertEqual(catalog1, catalog2)

    def test_get_movie(self):
        self.assertIsInstance(self.catalog.get_movie("The Dog"), Movie)
        self.assertIsNone(self.catalog.get_movie("A"))
        self.assertEqual("Mulan (2020)", str(self.catalog.get_movie("Mulan", 2020)))
