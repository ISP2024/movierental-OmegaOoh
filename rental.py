from movie import Movie
import pricing


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie: Movie,
                 days_rented: int,
                 price_code: pricing.PriceStrategy):
        """Initialize a new movie rental object for
        a movie with known rental period (daysRented).
        """
        if not isinstance(movie, Movie):
            raise TypeError("movie should be movie object")
        self.movie = movie
        if not isinstance(price_code, pricing.PriceStrategy):
            raise TypeError("price_code should be Pricing Strategy object")
        self.price_code = price_code
        self.days_rented = days_rented

    def get_movie(self) -> Movie:
        return self.movie

    def get_days_rented(self) -> int:
        return self.days_rented

    def get_price_code(self) -> pricing.PriceStrategy:
        """Returns Price code of the rentals"""
        return self.price_code

    def get_price(self) -> float:
        """Return rental price according to the movie type and duration."""
        return self.price_code.get_price(self.get_days_rented())

    def get_rental_points(self):
        """Returns rental price customer got for this rental"""
        return self.price_code.get_rental_points(self.get_days_rented())
