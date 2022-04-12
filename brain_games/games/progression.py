from random import randint
from typing import Tuple


def get_description() -> str:
    return 'What number is missing in the progression?'


def get_question_and_answer() -> Tuple[str]:
    length = 10
    start = randint(1, 20)
    step = randint(1, 5)
    hidden = randint(0, length - 1)
    progression = list(range(start, (start + length * step), step))
    correct_answer, progression[hidden] = str(progression[hidden]), '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
