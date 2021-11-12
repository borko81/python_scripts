import datetime

prices = {
    '00:00': 0,
    '00:05': 1,
    '01:01': 1,
    '02:01': 2,
    '03:01': 2.5
}


def generate_date():
    begin_date = datetime.datetime.now()
    stop_date = begin_date + datetime.timedelta(minutes=59)
    return begin_date, stop_date


def return_seconds_between_two_date(first, second):
    return (second - first).total_seconds()


def conv_to_zerofill(param):
    return str(param).zfill(2)


def hours_and_minutes_from_seconds(sec):
    hours = int(sec // 3600)
    minutes = int((sec % 3600) // 60)
    return f"{conv_to_zerofill(hours)}:{conv_to_zerofill(minutes)}"


def main():
    t = 0
    seconds = return_seconds_between_two_date(*generate_date())
    used_time = hours_and_minutes_from_seconds(seconds)
    try:
        t = [pr for (key, pr) in prices.items() if key > used_time][0]
    except IndexError:
        pass
    return t


print(main())