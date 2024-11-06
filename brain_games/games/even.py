"""Чётное ли число?"""

import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

# Глобальные переменные
MIN_NUMBER = 1
MAX_NUMBER = 100

def is_even(number):
    return number % 2 == 0

def make_question_and_correct_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
