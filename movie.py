from collections.abc import Collection
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """

    title: str
    year: int
    genre: Collection[str]

    def is_genre(self, genre: str) -> bool:
        """Returns true if movie contains given genre"""
        return genre.capitalize() in [i.capitalize() for i in self.genre]

    def __str__(self):
        return "{} ({})".format(self.title, self.year)
