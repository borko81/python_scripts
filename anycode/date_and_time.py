import datetime
from datetime import timedelta
import locale


d = datetime.datetime(2022, 3, 26)
after_days = d + timedelta(days=10)
print(after_days.strftime("%d.%m.%Y"))

# convert niz to datetime
text = "2022-03-26"
y = datetime.datetime.strptime(text, "%Y-%m-%d")
z = datetime.datetime.now()
print(y - z)

# work with locale
locale.setlocale(locale.LC_ALL, 'bulgarian')
z = datetime.datetime.now()
print(datetime.datetime.strftime(z, "%d.%m.%Y"))