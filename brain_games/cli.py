import prompt


def welcome():
	print('Welcome to the Brain Games!')


def get_name():
	return prompt.string('May i have your name? ')


def greet(name):
	print('Hello, {}!'.format(name))


def get_answer():
	return prompt.string('Your Answer: ')


def run():
	welcome()
	print()
	greet(get_name())