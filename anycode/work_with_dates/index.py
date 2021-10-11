from datetime import datetime, timedelta


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


start = datetime.now()
end = start + timedelta(days=1)

for d in date_range(start, end, timedelta(hours=1)):
    print(d)