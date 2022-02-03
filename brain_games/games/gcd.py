import prompt
from random import randint
from math import gcd


def gcd_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        correct_answer = gcd(number1, number2)
        print('Question: {} {}'.format(number1, number2))
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(."
                  "Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
