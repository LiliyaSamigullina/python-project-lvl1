import prompt
from random import randint


def is_prime(n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def prime_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    number_of_rounds = 3
    for _ in range(number_of_rounds):
        number = randint(2, 1000)
        print('Question: {}'.format(number))
        if is_prime(number) is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(."
                  "Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
