from random import randint
from typing import Tuple


def get_description() -> str:
    return 'Answer "yes" if the number is even, otherwise answer "no"'


def get_question_and_answer() -> Tuple[str]:
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
