from random import randint


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number in {0, 1}:
        return False
    for divider in range(2, int(number / 2) + 1):
        if number % divider == 0:
            return False
    return True


def get_question_and_answer():
    question = randint(0, 1000)
    if is_prime(question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
