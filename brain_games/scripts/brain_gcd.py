#!/usr/bin/env python
from brain_games.engine import run_game
from brain_games.games.gcd import description, get_question_and_answer


def main():
    run_game(get_question_and_answer, description)


if __name__ == '__main__':
    main()
