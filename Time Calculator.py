def add_time(start_time, duration, start_day=""):
    # Getting the values
    start_hour = int(start_time.split()[0].split(":")[0])
    start_minute = int(start_time.split()[0].split(":")[1])
    add_hour = int(duration.split(":")[0])
    add_minute = int(duration.split(":")[1])
    am_pm = start_time.split()[1]
    day = 0
    # Checking if AM or PM
    if am_pm == "PM":
        start_hour = start_hour + 12
    # Getting the result minute
    result_minute = start_minute + add_minute
    if result_minute > 60:
        result_minute = result_minute - 60
        pass_to_hour = 1  # If result_minute > 60 add 1 to result_hour
    else:
        pass_to_hour = 0
    result_minute = "{:02d}".format(result_minute)
    # Getting the result hour
    result_hour = start_hour + add_hour + pass_to_hour
    if result_hour > 24:
        while True:
            result_hour = result_hour - 24
            day += 1
            if result_hour < 24:
                break
    if result_hour > 12:
        result_hour = result_hour - 12
        half = "PM"
    elif result_hour == 12:
        if result_minute != 0:
            half = "PM"
        else:
            half = "AM"
    else:
        if result_hour == 0:
            result_hour = result_hour + 12
        half = "AM"
    if start_day == "":
        if day == 0:
            return str(result_hour) + ":" + str(result_minute) + " " + str(half)
        elif day == 1:
            return str(result_hour) + ":" + str(result_minute) + " " + str(half) + " (next day)"
        else:
            return str(result_hour) + ":" + str(result_minute) + " " + str(half) + " (" + str(day) + " days later)"
    else:
        week = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
        formatted_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        start_day = start_day.upper()
        start_index = week.index(start_day)
        skip = start_index + (day % 7)
        result_day = formatted_week[skip]
        if day == 0:
            return str(result_hour) + ":" + str(result_minute) + " " + str(half) + ", " + result_day
        elif day == 1:
            return str(result_hour) + ":" + str(result_minute) + " " + str(half) + ", " + result_day + " (next day)"
        else:
            return str(result_hour) + ":" + str(result_minute) + " " + str(half) + ", " + result_day + " (" + str(day) + " days later)"


add_time()
