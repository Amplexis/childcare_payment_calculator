from src.models.time import find_total_pay


def test__find_total_pay_should_return_1():
    start = 5
    end = 6

    total_pay = find_total_pay(start, end)

    assert total_pay == 15


def test__find_total_pay_should_return_2():
    start = 11
    end = 1

    total_pay = find_total_pay(start, end)

    assert total_pay == 40


def test__find_total_pay_should_return_2_for_2am_thru_4am():
    start = 2
    end = 4

    total_pay = find_total_pay(start, end)

    assert total_pay == 40


def test__find_total_pay_should_return_11_for_5pm_thru_4am():
    start = 5
    end = 4

    total_pay = find_total_pay(start, end)

    assert total_pay == 190



