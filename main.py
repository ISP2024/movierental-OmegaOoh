# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from pricing import NewPrice, RegularPrice, ChildrenPrice


def make_movies():
    """Some sample movies."""
    movies = [(
            Movie("Air", 2023, ["Drama", "Sport"]),
            NewPrice()
        ), (
            Movie("Oppenheimer", 2023, ["Biography", "Drama", "History"]),
            RegularPrice()
        ), (
            Movie("Frozen", 2013, ["Adventure", "Comedy", "Fantasy", "Musical"]),
            ChildrenPrice()
        ), (
            Movie("Bitconned", 2024, ["Documentary"]),
            NewPrice()
        ), (
            Movie("Particle Fever", 2013, ["Documentary"]),
            RegularPrice()
        )]
    return movies



if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie[0], days, movie[1]))
        days = (days + 2) % 5 + 1
    print(customer.statement())
