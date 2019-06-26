from src.models.time import validate_time_format
from src.models.family_rates import family_a_rates
from src.models.messages import *

def calculate_price_for_childcare(start_time, end_time):
    start_time_results = validate_time_format(start_time, "Start")
    end_time_results = validate_time_format(end_time, "End")
    print(start_time_results)
    print(end_time_results)

    if start_time_results[0] and end_time_results[0]:
        start_time = start_time_results[1]
        end_time = end_time_results[1]

        total_pay = 0

        while start_time < end_time:
            start_time += 1
            hourly_range_end = start_time

            for key in family_a_rates:
                if hourly_range_end in key:
                    total_pay += family_a_rates[key]

        return total_pay
    else:
        message = ""
        if start_time_results[0] is False and end_time_results is False:
            message += invalid_both
        elif start_time_results[0] is False:
            message += invalid_start_time
        elif end_time_results[0] is False:
            message += invalid_end_time
        return message

