#!/usr/bin/env python
from brain_games.common import common_game
from brain_games.games.progression import description, get_question_and_answer


def main():
    common_game(get_question_and_answer, description)


if __name__ == '__main__':
    main()
