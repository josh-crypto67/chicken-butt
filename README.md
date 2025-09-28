# chicken-butt
import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number!")

# Start the game
number_guessing_game()
