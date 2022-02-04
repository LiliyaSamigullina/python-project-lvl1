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
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(."
                  "Correct answer was '{}'".format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
