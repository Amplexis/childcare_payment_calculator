def find_number_of_hours(start_time, end_time):
    number_of_hours = 0

    if start_time in range(1, 5):
        start_time = convert_time(start_time)

    if end_time in range(1, 5):
        end_time = convert_time(end_time)

    while start_time < end_time:
        start_time += 1
        number_of_hours += 1

    return number_of_hours


def convert_time(end_time):
    end_time += 12
    return end_time
