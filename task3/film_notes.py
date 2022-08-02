from datatypes import Film

from typing import Iterable

import csv_service


class FilmNotes:
    @staticmethod
    def get(*args) -> list[Film]:
        raise NotImplementedError

    @staticmethod
    def add_film(*args) -> None:
        raise NotImplementedError

    @staticmethod
    def remove_film(*args) -> None:
        raise NotImplementedError

    @staticmethod
    def print_film(film: Film) -> None:
        print(
            f'Film - {film.film_name},'
            f' my note - {film.note}, my rating - {film.rating}'
        )

    @staticmethod
    def get_film_with_highest_rating(films: Iterable[Film]) -> Film:
        film_max_rating = max(films, key=lambda x: x.rating)

        return film_max_rating

    @staticmethod
    def get_film_with_lowest_rating(films: Iterable[Film]) -> Film:
        film_min_rating = min(films, key=lambda x: x.rating)

        return film_min_rating

    @staticmethod
    def get_average_rating_films(films: list) -> float:
        avg_rating = 0

        for film in films:
            avg_rating += film.rating

        return avg_rating / len(films)


class FilmNotesFromCSV(FilmNotes):
    @staticmethod
    def get(path_to_file: str) -> list[Film]:
        return csv_service.read_films_csv(path_to_file)

    @staticmethod
    def add_film(film: Film, path_to_file: str) -> None:
        csv_service.write_film_to_csv(
            film, path_to_file
        )

    @staticmethod
    def remove_film(film: Film, path_to_file: str) -> None:
        csv_service.delete_film_from_csv(film.film_name, path_to_file)
