from art import logo
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def difficulty():
    level = input("Choose a diffuculty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
def check_answer(number, answer, turns):
    if number > answer:
        print("Too high.")
        return turns - 1
    elif number < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    answer = randint(1 , 100)
    turns = difficulty()
    number = 0
    while (turns != 0 and number != answer):
        print(f"You have {turns} attempts remaining to guess the number.")
        number = int(input("Make a guess: "))
        turns = check_answer(number, answer, turns)

        if turns == 0:
          print("You've run out of guesses, you lose.")
          return
        elif number != answer:
          print("Guess again.")


game()