from random import randint


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def get_question_and_answer():
    question = randint(2, 1000)
    if is_prime(question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
