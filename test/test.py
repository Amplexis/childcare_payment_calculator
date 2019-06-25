from src.models.time import find_number_of_hours


def test__should_return_1():
    start = 5
    end = 6

    number_of_hours = find_number_of_hours(start, end)

    assert number_of_hours == 1
