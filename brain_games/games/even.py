"""Чётное ли число?"""

import random

def is_even(number):
    return number % 2 == 0

def make_question_and_correct_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
