from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def generate_qa_pair():
    op = ['-', '+', '*']
    task = '{} {} {}'.format(randint(0, 100), choice(op), randint(0, 100))
    result = str(eval(task))
    return (task, result)
