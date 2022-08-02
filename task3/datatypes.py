from dataclasses import dataclass
from typing import TypedDict


@dataclass
class Film:
    film_name: str
    note: str
    rating: float

    @staticmethod
    def _check_rating(rating: int):
        if not 1 <= rating <= 5:
            raise ValueError('Rating must be in the range of 1 to 5')

    def __setattr__(self, key, value):
        if key == 'rating':
            self._check_rating(value)

        super().__setattr__(key, value)
