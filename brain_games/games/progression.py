import prompt
from random import randint


def progression_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What number is missing in the progression?')
    print('Question: ', end='')
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        first_term = randint(1, 20)
        progression_diff = randint(1, 5)
        hidden = randint(1, 10)
        for i in range(10):
            term = first_term + i * progression_diff
            if i == hidden:
                print('..', end=' ')
                correct_answer = term
            else:
                print(term, end=' ')
        answer = prompt.string('\nYour answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(."
                  "Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
