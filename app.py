from src.models.time import validate_time

def calculate_price_for_childcare(start_time, end_time):
    start_time_results = validate_time(start_time)
    end_time_results = validate_time(end_time)

    if start_time_results[0] and end_time_results[0]:
        start_time = start_time_results[2]
        end_time = end_time_results[2]

        total_pay = 0
        if start_time >= 17:
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