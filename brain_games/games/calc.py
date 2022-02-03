import prompt
from random import randint, choice


def calc_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        operation = choice(['+', '-', '*'])
        if operation == '+':
            correct_answer = number1 + number2
        elif operation == '-':
            correct_answer = number1 - number2
        else:
            correct_answer = number1 * number2
        print('Question: {} {} {}'.format(number1, operation, number2))
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
