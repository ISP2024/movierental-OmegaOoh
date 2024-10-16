"""Strategy Class for pricing the movies"""
from abc import ABC, abstractmethod
from movie import Movie
from datetime import datetime


class PriceStrategy(ABC):
    """Abstract base class for rental pricing"""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of movie rental"""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class RegularPrice(PriceStrategy):
    """Rental Pricing for Regular Movie."""

    def get_price(self, days: int) -> float:
        """Two days for $2, additional days 1.50 per day."""
        return 2 + max(0, 1.5 * (days - 2))

    def get_rental_points(self, days: int) -> int:
        return 1


class ChildrenPrice(PriceStrategy):
    """Rental Pricing for Children Movie."""

    def get_price(self, days: int) -> float:
        """Three days for $1.50, additional days 1.50 per day."""
        return 1.5 + max(0, 1.5 * (days - 3))

    def get_rental_points(self, days: int) -> int:
        return 1


class NewPrice(PriceStrategy):
    """Rental Pricing for New Movie."""

    def get_price(self, days: int) -> float:
        """$3 per day"""
        return 3 * days

    def get_rental_points(self, days: int) -> int:
        """New release rentals earn 1 point for each day rented."""
        return days


def get_price_code_for_movie(movie: Movie):
    """
    Get price code of the movie.

    If the movie is release this year return NewPrice,
    Otherwise if it has "Children" or "Childrens" genre return ChildrenPrice,
    Otherwise return RegularPrice
    """
    if movie.year == datetime.year:
        return NewPrice()
    elif movie.is_genre("Children") or movie.is_genre("Childrens"):
        return ChildrenPrice()
    else:
        return RegularPrice()
