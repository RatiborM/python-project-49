"""НОД"""

import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

# Глобальные переменные
MIN_NUMBER = 1
MAX_NUMBER = 100

def calculate_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def make_question_and_correct_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(calculate_gcd(num1, num2))
    return question, correct_answer
