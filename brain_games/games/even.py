import prompt
from random import randint

def even_game():
  print('Welcome to the Brain Games!')
  name = prompt.string('May I have your name? ')
  print('Hello, {}!'.format(name))
  print('Answer "yes" if the number is even, otherwise answer "no"')
  number_of_rounds = 3
  for _ in range(number_of_rounds):
      number = randint(1, 100)
      print('Question: {}'.format(number))
      answer = prompt.string('Your answer: ')
      if (number % 2 == 0 and answer == 'yes') or (number % 2 == 1 and answer == 'no'):
        print('Correct!')
      elif number % 2 == 0 and answer != 'yes':      
        print("'{}' is wrong answer ;(. Correct answer was 'yes'".format(answer))
        print("Let's try again, {}!".format(name))
        break
      elif number % 2 == 1 and answer != 'no':
        print("'{}' is wrong answer ;(. Correct answer was 'no'.".format(answer))
        print("Let's try again, {}!".format(name))
        break
  else:
    print('Congratulations, {}!'.format(name))

  