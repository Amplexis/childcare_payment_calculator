from src.models.time import validate_time


def test__validate_time_should_return_true_and_int_of_17_when_validating_5_pm():
    time = "5 pm"

    results = validate_time(time)
    valid_time = results[0]
    time_int = results[1]

    assert valid_time
    assert time_int == 17


def test__validate_time_should_return_false_and_time_out_of_range_when_validating_4_pm():
    time = "4 pm"

    results = validate_time(time)
    valid_time = results[0]
    time_int = results[1]

    assert not valid_time
    assert time_int == "Time is out of range"


def test__validate_time_should_return_true_when_validating_12_am():
    time = "12 am"

    results = validate_time(time)
    valid_time = results[0]

    assert valid_time


def test__validate_time_should_return_false_for_fractional_hours():
    time = "6:15 pm"

    results = validate_time(time)
    valid_time = results[0]

    assert not valid_time


def test__validate_time_should_return_true_when_validating_3_00_AM():
    time = "3:00 AM"

    results = validate_time(time)
    valid_time = results[0]

    assert not valid_time
