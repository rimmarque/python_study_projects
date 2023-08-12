import random


def rockPaperScissorsLizardSpock():
    user = input("What's your choice: rock, paper or scissors, lizard or Spock? ")
    computer = random.choice(["rock", "paper", "scissors", "lizard", "Spock"])
    print(
        f"Your choice is {user} and computer's choise is {computer}! Let the play begin!"
    )

    if user == computer:
        print("It's a tie!")
    elif user == "rock":
        if computer == "scissors" or computer == "lizard":
            youWon()
        else:
            youLost()
    elif user == "paper":
        if computer == "rock" or computer == "Spock":
            youWon()
        else:
            youLost()
    elif user == "scissors":
        if computer == "paper" or computer == "lizard":
            youWon()
        else:
            youLost()
    elif user == "lizard":
        if computer == "paper" or computer == "Spock":
            youWon()
        else:
            youLost()
    elif user == "Spock":
        if computer == "scissors" or computer == "rock":
            youWon()
        else:
            youLost()


def youWon():
    print("Congratulations! You won " + str(random.randint(1, 1000000)) + " coins!")


def youLost():
    print("You lost everything!")


rockPaperScissorsLizardSpock()
