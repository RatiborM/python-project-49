"""Арифметическая прогрессия"""

from random import randint

# Глобальные переменные
PROGRESSION_LENGTH = 10
MIN_START = 1
MAX_START = 10
MIN_STEP = 1
MAX_STEP = 5

DESCRIPTION = 'What number is missing in the progression?'


def make_progression(progression_len,
                     min_step, max_step,
                     min_first_num, max_first_num):
    """Generate arithmetic progression."""
    first_num = randint(min_first_num, max_first_num)
    progression_step = randint(min_step, max_step)
    progression = [first_num, ]
    for _ in range(progression_len - 1):  # коррекция цикла для точной длины
        next_num = first_num + progression_step
        progression.append(next_num)
        first_num = next_num
    return progression


def make_question_and_correct_answer():
    """Make game question and answer."""
    # Используем глобальные переменные
    progression = make_progression(
        progression_len=PROGRESSION_LENGTH,
        min_step=MIN_STEP,
        max_step=MAX_STEP,
        min_first_num=MIN_START,
        max_first_num=MAX_START
    )
    random_index = randint(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
