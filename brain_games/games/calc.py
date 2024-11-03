import random
import operator

DESCRIPTION = "What is the result of the expression?"

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

def generate_question_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(list(OPERATIONS.keys()))

    question = f"{num1} {operation} {num2}"
    correct_answer = str(OPERATIONS[operation](num1, num2))

    return question, correct_answer