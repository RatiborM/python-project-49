#!/usr/bin/env python3
import random

def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 100)

        print(f"Question: {number}")

        user_answer = input("Your answer: ")

        if (number % 2 == 0 and user_answer == "yes") or (number % 2 != 0 and user_answer == "no"):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was {'no' if number % 2 != 0 else 'yes'}.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers == 3:
        print(f"Congratulations, {name}!")

def main():
    play_game()

if __name__ == '__main__':
    main()