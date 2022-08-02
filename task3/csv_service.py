import os
import csv

import exc
from datatypes import Film


def check_path_exist(path: str) -> None:
    if not os.path.exists(path):
        raise exc.DirectoryNotExist(f'Given path is not valid - {path}')


def read_films_csv(path_to_file: str) -> list[Film]:
    check_path_exist(path_to_file)

    films = []
    with open(path_to_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        for row in reader:
            films.append(
                Film(row['film_name'], row['note'], float(row['rating']))
            )

    return films


def _write_film(writer: csv.DictWriter, film: Film):
    writer.writerow(
        {'film_name': film.film_name, 'note': film.note, 'rating': film.rating}
    )


def write_film_to_csv(film: Film, path_to_file: str, mode=None) -> None:
    if mode is None:
        mode = 'a' if os.path.exists(path_to_file) else 'w'

    with open(path_to_file, mode) as csvfile:
        fieldnames = ['film_name', 'note', 'rating']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if mode == 'w':
            writer.writeheader()

        _write_film(writer, film)


def _remove_film_from_list(film_name: str, films: list[Film]) -> list[Film]:
    new_films = []

    for film in films:
        if film.film_name != film_name:
            new_films.append(film)

    return new_films


def delete_film_from_csv(film_name: str, path_to_file: str) -> None:
    films = read_films_csv(path_to_file)

    new_films = _remove_film_from_list(film_name, films)

    write_film_to_csv(new_films[0], path_to_file, mode='w')
    for film in new_films[1:]:
        write_film_to_csv(film, path_to_file)
