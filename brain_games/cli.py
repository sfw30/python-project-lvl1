import prompt

def welcome_user():
	name = prompt.string('May i have your name? ')
	print('Hello, ' + name + '!')