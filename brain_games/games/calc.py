import operator
from random import randint, choice


def get_description():
    return 'What is the result of the expression?'


def get_question_and_answer():
    operand_left = randint(1, 100)
    operand_right = randint(1, 100)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    operation = choice(list(operations.keys()))
    question = '{} {} {}'.format(operand_left, operation, operand_right)
    correct_answer = str(operations[operation](operand_left, operand_right))
    return question, correct_answer
