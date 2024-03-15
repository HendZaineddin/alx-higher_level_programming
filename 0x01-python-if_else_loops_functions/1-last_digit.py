#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def lastdigit(number):
    if number < 0:
        return (number % -10)
    else:
        return (number % 10)


if lastdigit(number) > 5:
    print('Last digit of', number, 'is', lastdigit(number), 'and is greater than 5')
elif lastdigit(number) == 0:
    print('Last digit of', number, 'is', lastdigit(number), 'and is 0')
elif lastdigit(number) < 6 and lastdigit(number) != 0:
    print('Last digit of', number, 'is', lastdigit(number), 'and is less than 6 and not 0')
