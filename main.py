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
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess the number.")

    # Loop until the user guesses the correct number or runs out of attempts
    while attempts < max_attempts:
        try:
            # Show current attempt number 
            print(f"Attempt {attempts + 1} of {max_attempts}")
            # Get user input
            user_guess = int(input("Enter your guess: "))
            # error handling for out of range guesses
            if user_guess < 1 or user_guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue
            # Increment attempt count
            attempts += 1
            # Check if the guess is correct, too high, or too low
            if user_guess == number:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                # Win score
                return True 
            elif user_guess < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        # Handle non-integer inputs
        except ValueError:
            print("Please enter a valid number.")
        
    # If the user fails to guess the number within the allowed attempts
    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number}.")
        # Lost score
        return False 

# Function to play the game again and track scores/games played
def play_game():
    print("Welcome to Guess the Number!")
    games_played = 0
    wins = 0
    #loop to follow scores/games played
    while True:
        won = guess_the_number()
        games_played += 1
        if won:
            wins += 1
        print(f"\n Games played: {games_played} | Wins: {wins}")
       # Loop to play again or exit 
        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print(f"\nFinal Score: {wins} wins out of {games_played} games played.")
                print("Thanks for playing! Goodbye!")
                return
            # Handle invalid input 
            else:
                print("Please enter 'yes' or 'no'.")
        
# Run the game
if __name__ == "__main__":
    play_game()
