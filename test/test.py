from src.models.time import validate_time_format
from app import calculate_price_for_childcare

def test__validate_time_format_should_return_true_and_int_of_17_when_validating_5_pm_start_time():
    time = "5 pm"
    type = "Start"
    family = "A"

    results = validate_time_format(time, type)
    valid_time = results[0]
    time_int = results[1]

    assert valid_time
    assert time_int == 17


def test__validate_time_format_should_return_false_and_time_out_of_range_when_validating_4_pm_start_time():
    time = "4 pm"
    type = "Start"
    family = "A"

    results = validate_time_format(time, type)
    valid_time = results[0]
    time_int = results[1]

    assert not valid_time
    assert time_int == "Time is out of range"


def test__validate_time_format_should_return_true_when_validating_12_am_start_time():
    time = "12 am"
    type = "Start"
    family = "A"

    results = validate_time_format(time, type)
    valid_time = results[0]

    assert valid_time


def test__validate_time_format_should_return_false_for_fractional_hours_start_time():
    time = "6:15 pm"
    type = "Start"
    family = "A"

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


def test__validate_time_format_should_return_false_for_5_pm_end_time():
    time = "5 pm"
    type = "End"

    results = validate_time_format(time, type)
    valid_time = results[0]

    assert not valid_time


def test__should_return_75_for_family_a_from_5_pm_to_10_pm():
    start = "5 pm"
    end = "10 pm"
    family = "A"

    result = calculate_price_for_childcare(start, end, family)

    assert result == 75


def test__should_return_invalid_start_time_msg_when_calculate_price_for_childcare_is_given_4_pm_start_time():
    start = "4 pm"
    end = "6 pm"
    family = "A"

    result = calculate_price_for_childcare(start, end, family)

    assert result == "Start time is invalid"


def test__should_return_invalid_end_time_msg_when_calculate_price_for_childcare_is_given_3_pm_end_time():
    start = "10 pm"
    end = "3 pm"
    family = "A"

    result = calculate_price_for_childcare(start, end, family)

    assert result == "End time is invalid"

def test__should_return_both_invalid_time_message_when_calculate_price_for_childcare_is_given_10_am_start_and_11_am_end():
    start = "10 am"
    end = "11 am"
    family = "A"

    result = calculate_price_for_childcare(start, end, family)

    assert result == "Both times are out of range"

def test__should_return_70_for_family_A_given_start_of_9_pm_and_end_of_1_am():
    start = "9 pm"
    end = "1 am"
    family = "A"

    result = calculate_price_for_childcare(start, end, family)

    assert result == 70


def test_should_return_190_for_family_A_given_start_of_5_pm_and_end_of_4_am():
    start = "5 pm"
    end = "4 am"
    family = "A"

    result = calculate_price_for_childcare(start, end, family)

    assert result == 190


def test_should_return_52_for_family_B_given_start_of_7_pm_and_end_of_12_am():
    start = "7 pm"
    end = "12 am"
    family = "B"

    result = calculate_price_for_childcare(start, end, family)

    assert result == 52


def test_should_return_140_for_family_B_given_start_of_5_pm_and_end_of_4_am():
    start = "5 pm"
    end = "4 am"
    family = "B"

    result = calculate_price_for_childcare(start, end, family)

    assert result == 140