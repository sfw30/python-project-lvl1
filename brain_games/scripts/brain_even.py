import random
import prompt
from brain_games.logic.constants import NAME


def even_check():
	print('Answer "yes" if the number is even, otherwise answer "no"')
	correct = 0
	while correct < 3:
		question = random.randint(1, 20)
		print(f'Question: {question}')
		answer = prompt.string('Your answer: ').strip()
		if answer == 'yes' and question % 2 == 0:
			print('Correct!')
		elif answer == 'no' and question % 2 != 0:
			print('Correct!')
		elif answer == 'yes' and question % 2 != 0:
			print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
			break 
		elif answer == 'no' and question % 2 == 0:
			print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
			break
		else:
			print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
			
			break
		correct += 1
	return print(f'Congratulation, {NAME}!' if correct == 3 else f"Lets try again, {NAME}!")