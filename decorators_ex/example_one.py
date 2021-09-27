# High order function


def sum(n, func):
    total = 0
    for number in range(n + 1):
        total += (func(number))
    return total


def square(n):
    return n * n


result = sum(10, square)

# Nested function

from random import choice


def greet(person):
    def get_mood():
        mood_result = choice(['One', 'Two', 'Three'])
        return mood_result
    return get_mood() + ' ' + person


print(greet('Person One'))
