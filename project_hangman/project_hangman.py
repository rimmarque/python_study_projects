import random
from words import words
import string
from hangman_pics import hangman_pics


def getValidWord(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangmanGame():
    word = getValidWord(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters user has guessed
    lives = 6
    count = 0

    while len(word_letters) > 0 and lives > 0:
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("The word is ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if len(user_letter) > 1 and user_letter in alphabet:
            print("Please input only 1 letter at a time")
        elif user_letter in used_letters:
            print("You already guessed this letter. Please try another letter")
        elif user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("The letter is not in word")
                print(hangman_pics[count])
                count = count + 1
        else:
            print("Invalid character. Try a letter not a symbol")

        print(
            f"You have {lives} lives left. Be careful! You have used these letters: ",
            " ".join(used_letters),
        )
    if lives == 0:
        print("You lost! The word is " + word)
        print(hangman_pics[6])
    else:
        print("You won! The word is " + word.upper())


hangmanGame()
