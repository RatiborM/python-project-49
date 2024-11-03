#!/usr/bin/env python3
import random
import math

def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    correct_answers = 0

    while correct_answers < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        print(f"Question: {num1} {num2}")
        user_answer = input("Your answer: ")

        correct_answer = math.gcd(num1, num2)

        if int(user_answer) == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers == 3:
        print(f"Congratulations, {name}!")

def main():
    play_game()

if __name__ == '__main__':
    main()