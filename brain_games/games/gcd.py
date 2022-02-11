from random import randint
from math import gcd


description = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = '{} {}'.format(number1, number2)
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer
