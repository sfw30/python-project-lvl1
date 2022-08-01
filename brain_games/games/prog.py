from random import choice
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_qa_pair():
	start = randint(0, 100)
	l = [start]
	prog = randint(1, 10)
	for _ in range(9):
		l.append(l[-1] + prog)
	result = choice(l)
	i = l.index(result)
	task = l[:i]+['..']+l[i+1:]
	task = ' '.join(map(str,task))
	return (task, str(result))


