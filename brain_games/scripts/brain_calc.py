#!/usr/bin/env python
from brain_games.common import run_game
from brain_games.games.calc import description, get_question_and_answer


def main():
    run_game(get_question_and_answer, description)


if __name__ == '__main__':
    main()
