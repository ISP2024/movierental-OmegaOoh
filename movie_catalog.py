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
        self.read_csv()

    def read_csv(self):
        with open("movies.csv", "r") as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                if line[0].startswith("#") or line[0].isspace():
                    # Skip comment and blank lines
                    continue
                try:
                    self.catalog.append(
                        Movie(
                            line[1],
                            int(line[2]),
                            line[3].split("|"),
                        ))
                except (ValueError, TypeError, IndexError):
                    logger.error(f'Line {csv_file.line_num}: Unrecognized format "{", ".join(line)}"')

    def get_movie(self, title: str, year: int = None):
        """Get movie object by name and year."""
        for movie in self.catalog:
            if title == movie.title:
                if year is None or movie.year == year:
                    return movie
        return None  # Movie doesn't in the catalog.
