import prompt


def run_game(game) -> None:
    GAME_ROUNDS_COUNTER = 3
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game.get_description())
    for _ in range(GAME_ROUNDS_COUNTER):
        question, correct_answer = game.get_question_and_answer()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(."
                  "Correct answer was '{1}'".format(user_answer, correct_answer))
            print("Let's try again, {}!".format(user_name))
            break
    else:
        print('Congratulations, {}!'.format(user_name))
