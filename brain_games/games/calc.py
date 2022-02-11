from random import randint, choice


description = 'What is the result of the expression?'


def get_question_and_answer():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operation = choice(['+', '-', '*'])
    question = '{} {} {}'.format(number1, operation, number2)
    if operation == '+':
        correct_answer = str(number1 + number2)
    elif operation == '-':
        correct_answer = str(number1 - number2)
    else:
        correct_answer = str(number1 * number2)
    return question, correct_answer
