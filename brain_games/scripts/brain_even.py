#!/usr/bin/env python
"""Запуск для четное или нет"""


from brain_games.engine import run_game
from brain_games.games import even


def main():
    """Start the "Brain-Even Game"."""
    run_game(even)


if __name__ == '__main__':
    main()
