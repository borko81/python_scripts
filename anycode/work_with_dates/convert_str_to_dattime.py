from datetime import datetime

text = '2021-10-04'

# convert str to datetime
d = datetime.strptime(text, "%Y-%m-%d")

# convert datetime to human readable format
n = datetime.now()
human_n = datetime.strftime(n, "%d.%m.%Y")

# convert utc time to localtime
u = datetime.utcnow()
print(u)
