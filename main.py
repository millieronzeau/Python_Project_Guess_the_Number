# Load the import random module 
import random

# Function for Guess the Number Game scaffold 
def guess_the_number():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    # Set maximum attempts
    max_attempts = 10
    attempts = 0

    # Game introduction
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess the number.")

    # Loop until the user guesses the correct number
    while attempts < max_attempts:
        try:
            # Get user input
            user_guess = int(input("Enter your guess: "))
            attempts += 1
           
            # Check if the guess is correct, too high, or too low
            if user_guess == number:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                break
            elif user_guess < number:
                print("Too low! Try again.")
            else: 
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid integer.")
    # If the user fails to guess the number within the allowed attempts
    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number}.")

# Run the game
if __name__ == "__main__":
    guess_the_number()

