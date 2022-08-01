from random import choice
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_qa_pair():
    start = randint(0, 100)
    list = [start]
    prog = randint(1, 10)
    for _ in range(9):
        list.append(list[-1] + prog)
    result = choice(list)
    i = list.index(result)
    task = list[:i] + ['..'] + list[i + 1:]
    task = ' '.join(map(str, task))
    return (task, str(result))
