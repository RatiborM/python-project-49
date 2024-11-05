#!/usr/bin/env python
"""Запуск для простого числа"""


from brain_games.engine import run_game
from brain_games.games import prime


def main():
    """Start the "Brain-Prime Game"."""
    run_game(prime)


if __name__ == '__main__':
    main()
