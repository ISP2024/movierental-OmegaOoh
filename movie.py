from abc import ABC, abstractmethod
import enum

class PriceStrategy(ABC):
    """Abstract base class for rental pricing"""

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


class Movie:
    """
    A movie available for rent.
    """

    REGULAR = RegularPrice()
    NEW_RELEASE = NewPrice()
    CHILDRENS = ChildrenPrice()

    def __init__(self, title, price_code):
        # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_price_code(self) -> PriceStrategy:
        # get the price code
        return self.price_code
    
    def get_title(self):
        return self.title
    
    def get_price(self, days):
        """Get rental price of movie by days"""
        return self.get_price_code().get_price(days)
    
    def get_rental_points(self, days):
        """Get rental point of movie by days"""
        return self.get_price_code().get_rental_points(days)
    
    def __str__(self):
        return self.title

