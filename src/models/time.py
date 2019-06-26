def validate_time_format(time_to_validate, type):
    results = []
    valid_time = False

    valid_format = "%I %p"
    string_start_time = time_to_validate

    try:
        import time
        valid_time = time.strptime(string_start_time, valid_format)
        valid = True
    except Exception as e:
        print(e)
        valid = False

    results.append(valid)

    if valid_time:
        result = validate_time_range(valid_time, type)

        if result is False:
            results[0] = False
            results.append("Time is out of range")
        else:
            results.append(result)

    return results


def validate_time_range(valid_time, type):
    time = valid_time.tm_hour

    if type == "Start":
        if time >= 17 or time <= 3:
            result = time
        else:
            result = False
    else:
        if time >= 18 or time <= 4:
            result = time
        else:
            result = False

    return result




