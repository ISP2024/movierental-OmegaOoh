# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from pricing import NewPrice, RegularPrice, ChildrenPrice


def make_movies():
    """Some sample movies."""
    movies = [
        (Movie("Air"), NewPrice()),
        (Movie("Oppenheimer"), RegularPrice()),
        (Movie("Frozen"), ChildrenPrice()),
        (Movie("Bitconned"), NewPrice()),
        (Movie("Particle Fever"), RegularPrice())
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie[0], days, movie[1]))
        days = (days + 2) % 5 + 1
    print(customer.statement())
