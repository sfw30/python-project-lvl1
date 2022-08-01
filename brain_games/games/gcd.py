from math import gcd
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_qa_pair():
    task = '{} {}'.format(randint(0, 100), randint(0, 100))
    gcd_numbers = task.split(' ')
    result = str(gcd(int(gcd_numbers[0]), int(gcd_numbers[1])))
    return (task, result)
