#!/usr/bin/env python
from brain_games.engine import run_game
from brain_games.games import even


def main() -> None:
    run_game(even)


if __name__ == '__main__':
    main()
