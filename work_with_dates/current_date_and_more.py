import time
from time import gmtime, strftime

from datetime import datetime, timedelta

t = time.localtime()
print(strftime("%d/%m/%Y %H:%M", t))

# Convert seconds to minutes
s = 86400
print(s / 60)

# Convert string to datetime
my_time = "2021-11-01"
print(datetime.strptime(my_time, "%Y-%m-%d"))

delta = timedelta(seconds=s)
print(delta)

# Found days between two date
date_one = "2021-10-31 18:50"
date_two = "2021-11-01 20:40"

FORMAT = "%Y-%m-%d %H:%M"

diff =  datetime.strptime(date_two, FORMAT) - datetime.strptime(date_one, FORMAT)
diff_seconds = diff.total_seconds()

print(timedelta(seconds=diff_seconds) + timedelta(hours=10))

# Get dat seven days before current date
current_date = "2021-11-01"
SEVEN_DAYS_BEFORE = 7
current_date_to_datetime = datetime.strptime(current_date, "%Y-%m-%d")
seven_day_before_current_date = current_date_to_datetime - timedelta(days=SEVEN_DAYS_BEFORE)
print(current_date_to_datetime)
print(str(seven_day_before_current_date).split()[0])
