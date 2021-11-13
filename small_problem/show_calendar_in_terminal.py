import calendar
import os

year = int(input("Enter year :"))
month = int(input("Enter month :"))

os.system('cls')
calendar = calendar.month(year, month)

print(calendar)
