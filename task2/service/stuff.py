import os

import exc


def check_path_exist(path: str) -> None:
    if not os.path.exists(path):
        raise exc.DirectoryNotExist(f'Given path is not valid - {path}')


def save_file(file: bytes, directory: str, filename) -> None:
    check_path_exist(directory)

    with open(f'{directory}/{filename}', 'wb') as open_file:
        open_file.write(file)
