def hash_string(string: str, multiple_constant: int = 51) -> int:
    result_hash = 0

    for char in string:
        result_hash = multiple_constant * result_hash + ord(char)

    return result_hash


if __name__ == '__main__':
    test_string = 'Python Bootcamp'

    print(hash_string(test_string))
