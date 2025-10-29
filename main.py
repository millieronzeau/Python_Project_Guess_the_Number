# Load the import random module 
import random

# Function for Guess the Number Game scaffold 
def guess_the_number():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")

    # Loop until the user guesses the correct number
    while True:
        try:
            # Get user input
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            # Check if the guess is correct, too high, or too low
            if user_guess < number:
                print("Too low! Try again.")
            elif user_guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
if __name__ == "__main__":
    guess_the_number()

