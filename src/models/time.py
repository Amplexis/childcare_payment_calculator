import time

def convert_time(end_time):
    end_time += 12
    return end_time


def validate_time(time_to_validate):
    results = []
    valid_time = False

    valid_format = "%I %p"
    string_start_time = time_to_validate

    try:
        valid_time = time.strptime(string_start_time, valid_format)
        valid = True
    except Exception as e:
        print(e)
        valid = False

    results.append(valid)
    if valid_time:
        results.append(valid_time.tm_hour)

    return results
