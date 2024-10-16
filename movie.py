import pricing


class Movie:
    """
    A movie available for rent.
    """

    REGULAR = pricing.RegularPrice()
    NEW_RELEASE = pricing.NewPrice()
    CHILDRENS = pricing.ChildrenPrice()

    def __init__(self, title, price_code):
        # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_price_code(self) -> pricing.PriceStrategy:
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    def get_price(self, days):
        """Get rental price of movie by days"""
        return self.price_code.get_price(days)

    def get_rental_points(self, days):
        """Get rental point of movie by days"""
        return self.price_code.get_rental_points(days)

    def __str__(self):
        return self.title

