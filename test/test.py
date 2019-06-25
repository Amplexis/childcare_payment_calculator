from src.models.time import validate_time


def test__should_return_true_and_int_of_17_when_validating_5_pm():
    time = "5 pm"

    results = validate_time(time)
    valid_time = results[0]
    time_int = results[1]

    assert valid_time
    assert time_int == 17



