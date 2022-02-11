from random import randint


description = 'What number is missing in the progression?'


def get_question_and_answer():
    first_term = randint(1, 20)
    progression_diff = randint(1, 5)
    hidden = randint(0, 9)
    question = ''
    for i in range(10):
        term = first_term + i * progression_diff
        if i == hidden:
            question += '.. '
            correct_answer = str(term)
        else:
            question = question + str(term) + ' '
    return question.rstrip(), correct_answer
