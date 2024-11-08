"""Калькулятор"""

import random

DESCRIPTION = 'What is the result of the expression?'

MIN_NUMBER = 1
MAX_NUMBER = 10
OPERATORS = ['+', '-', '*']


def calculate(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def make_question_and_correct_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = f"{num1} {operator} {num2}"
    correct_answer = str(calculate(operator, num1, num2))
    return question, correct_answer
