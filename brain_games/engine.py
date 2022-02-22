import prompt


def run_game(get_question_and_answer, description):
    game_rounds_counter = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(description)
    for _ in range(game_rounds_counter):
        question, correct_answer = get_question_and_answer()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(."
                  "Correct answer was '{}'".format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
