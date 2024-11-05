#!/usr/bin/env python
"""Запуск для калькулятора"""


from brain_games.engine import run_game
from brain_games.games import calc


def main():
    """Start the "Brain-Calc Game"."""
    run_game(calc)


if __name__ == '__main__':
    main()
