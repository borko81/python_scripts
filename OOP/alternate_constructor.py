import time


class mDate:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = mDate(2021, 10, 10)
b = mDate.today()
print(a.__dict__)
print(b.__dict__)
