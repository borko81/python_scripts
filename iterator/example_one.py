my_list = [1, 2, 3, 4, 5]

my_iter = iter(my_list)

# print(my_iter.__next__())

# while True:
#     try:
#         print(my_iter.__next__())
#     except StopIteration:
#         break


class PowTwo:

    def __init__(self, inc, max=0):
        self.max = max
        self.inc = inc

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if not self.n > self.max:
            result = self.inc * self.n
            self.n += 1
            return result
        raise StopIteration


p = PowTwo(4, 5)
for i in p:
    print(i)
