from src.models.time import find_number_of_hours


def test__find_number_of_hours_should_return_1():
    start = 5
    end = 6

    number_of_hours = find_number_of_hours(start, end)

    assert number_of_hours == 1


def test__find_number_of_hours_should_return_2():
    start = 11
    end = 1

    number_of_hours = find_number_of_hours(start, end)

    assert number_of_hours == 2


def test__find_number_of_hours_should_return_2_for_2am_thru_4am():
    start = 2
    end = 4

    number_of_hours = find_number_of_hours(start, end)

    assert number_of_hours == 2
