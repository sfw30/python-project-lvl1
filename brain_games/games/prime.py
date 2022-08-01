from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
	return (number % 2) == 0
	

def generate_qa_pair():
	number = randint(0, 100)
	prime = 'no' if is_prime(number) else 'yes'
	return(number, prime)
