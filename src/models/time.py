from src.models.family_rates import family_a_rates

def find_total_pay(start_time, end_time):
    total_pay = 0

    if start_time in range(1, 5):
        start_time = convert_time(start_time)

    if end_time in range(1, 5):
        end_time = convert_time(end_time)

    while start_time < end_time:
        start_time += 1
        hourly_range_end = start_time

        for key in family_a_rates:
            if hourly_range_end in key:
                total_pay += family_a_rates[key]

    return total_pay


def convert_time(end_time):
    end_time += 12
    return end_time
