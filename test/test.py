from src.models.time import validate_time_format


def test__validate_time_format_should_return_true_and_int_of_17_when_validating_5_pm_start_time():
    time = "5 pm"
    type = "Start"

    results = validate_time_format(time, type)
    valid_time = results[0]
    time_int = results[1]

    assert valid_time
    assert time_int == 17


def test__validate_time_format_should_return_false_and_time_out_of_range_when_validating_4_pm_start_time():
    time = "4 pm"
    type = "Start"

    results = validate_time_format(time, type)
    valid_time = results[0]
    time_int = results[1]

    assert not valid_time
    assert time_int == "Time is out of range"


def test__validate_time_format_should_return_true_when_validating_12_am_start_time():
    time = "12 am"
    type = "Start"

    results = validate_time_format(time, type)
    valid_time = results[0]

    assert valid_time


def test__validate_time_format_should_return_false_for_fractional_hours_start_time():
    time = "6:15 pm"
    type = "Start"

    results = validate_time_format(time, type)
    valid_time = results[0]

    assert not valid_time


def test__validate_time_format_should_return_true_when_validating_3_00_AM_start_time():
    time = "3:00 AM"
    type = "Start"

    results = validate_time_format(time, type)
    valid_time = results[0]

    assert not valid_time


def test__validate_time_format_should_return_true_for_6_pm_end_time():
    time = "6 pm"
    type = "End"

    results = validate_time_format(time, type)
    valid_time = results[0]

    assert valid_time

def test__validate_time_format_should_return_false_for_5_pm_end_time():
    time = "5 pm"
    type = "End"

    results = validate_time_format(time, type)
    valid_time = results[0]

    assert not valid_time