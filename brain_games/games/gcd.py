from random import randint
from math import gcd
from typing import Tuple


def get_description() -> str:
    return 'Find the greatest common divisor of given numbers.'


def get_question_and_answer() -> Tuple[str]:
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = '{0} {1}'.format(number1, number2)
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer
