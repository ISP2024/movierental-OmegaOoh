from movie import Movie
import csv
import logging

logger = logging.getLogger()


class MovieCatalog():
    """Catalog of movies from movies.csv file"""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Create Movie Catalog from csv file"""
        self.catalog = []
        self.movie_gen = self.read_csv()

    def read_csv(self):
        """Generator Function to read movies from csv files."""
        with open("movies.csv", "r") as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                if line[0].startswith("#") or line[0].isspace():
                    # Skip comment and blank lines
                    continue
                try:
                    yield Movie(
                                    line[1],
                                    int(line[2]),
                                    line[3].split("|")
                                )
                except (ValueError, TypeError, IndexError):
                    logger.error(f'Line {csv_file.line_num}: Unrecognized format "{", ".join(line)}"')

    def movie_match(self, movie: Movie, title: str, year: int) -> bool:
        """Check if movie match the criteria"""
        return title == movie.title and (year is None or movie.year == year)

    def get_movie(self, title: str, year: int = None):
        """Get movie object by name and year."""
        # Find movie from catalog
        for movie in self.catalog:
            if self.movie_match(movie, title, year):
                return movie

        # Find movie from generator instead
        for movie in self.movie_gen:
            self.catalog.append(movie)
            if self.movie_match(movie, title, year):
                return movie

        return None
