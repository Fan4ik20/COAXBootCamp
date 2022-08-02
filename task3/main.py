from datatypes import Film
from film_notes import FilmNotesFromCSV


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
