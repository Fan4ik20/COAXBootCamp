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


def main() -> None:
    path_to_csv = 'data/films.csv'

    films = [
        Film('Winter in Fire', 'about freedom', 4.5),
        Film('Cyborgs', 'about brave people', 5),
        Film('Gareth Jones', 'about dark times', 4)
    ]

    for film in films:
        FilmNotesFromCSV.add_film(film, path_to_csv)

    films_from_csv = FilmNotesFromCSV.get(path_to_csv)
    print('Films From CSV')
    for film in films_from_csv:
        FilmNotesFromCSV.print_film(film)

    print('-' * 15)

    film_to_remove = films[0]
    FilmNotesFromCSV.remove_film(film_to_remove, path_to_csv)

    films_from_csv_after_deleting = FilmNotesFromCSV.get(path_to_csv)
    print('Films From CSV after deleting')
    for film in films_from_csv_after_deleting:
        FilmNotesFromCSV.print_film(film)

    print('-' * 15)

    highest_rating = FilmNotesFromCSV.get_film_with_highest_rating(films)
    print('Film with highest rating')
    FilmNotesFromCSV.print_film(highest_rating)
    print('-' * 15)

    print('Film with lowest rating')
    lowest_rating = FilmNotesFromCSV.get_film_with_lowest_rating(films)
    FilmNotesFromCSV.print_film(lowest_rating)

    average_rating = FilmNotesFromCSV.get_average_rating_films(films)
    print('Average rating')
    print(average_rating)


if __name__ == '__main__':
    main()
