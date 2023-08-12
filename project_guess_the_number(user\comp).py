import random


def guessNumber(end_number):
    random_number = random.randint(1, end_number)
    answer = 0
    while answer != random_number:
        answer = int(input(f"Guess a number between 1 and {end_number}: "))
        if answer < random_number:
            print("Guess again. Too low.")
        elif answer > random_number:
            print("Guess again. Too high.")
        else:
            print("You won!")


def computerGuessNumber(end_number):
    low_border = 1
    high_border = end_number
    feedback = ""
    print(
        f"Think of a random number between 1 and {end_number}. Now answer some questions and I will guess the number :) "
    )
    while feedback != "correct":
        if low_border != high_border:
            answer = random.randint(low_border, high_border)
        else:
            answer = low_border
        feedback = input(f"Is {answer} too high, too low, or correct? ")
        if feedback == "too high":
            high_border = answer - 1
        elif feedback == "too low":
            low_border = answer + 1
        else:
            print(f"I won! The number you thought about is {answer}.")


guessNumber(10)
computerGuessNumber(10)
