#  Import the random module to generate a random number 
import random


def guess_the_number():
    """ Runs one round of the 'Guess the Number' game.
    Generates a random number between 1 and 100.
    Prompts the player to guess, provides feedback and tracks attempts.
    Returns True if the player wins, False otherwise.
    """

    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    # Set maximum number of attempts
    max_attempts = 10
    attempts = 0

    # Game introduction
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess the number.")

    # Loop until the user guesses the correct number or runs out of attempts
    while attempts < max_attempts:
        try:
            # Show current attempt number 
            print(f"\nAttempt {attempts + 1} of {max_attempts}")
            
            # Get user input
            user_guess = int(input("Enter your guess: "))
           
            # Validate the guess is within range
            if user_guess < 1 or user_guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue # Skip incerementing attempts for invalid input

            # Increment attempt count
            attempts += 1

            # Check if the guess is correct, too high, or too low
            if user_guess == number:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                return True  # Win score
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
        return False  # Lost score

def play_game():
    """ Main loop for the 'Guess the Number' game. 
    Tracks the total games played and wins.
    Prompts the user to play again or exit.
    """
    print("Welcome to Guess the Number!")
    # Initialise counters for statistics 
    games_played = 0
    wins = 0

    # Main game loop continuing until the user decides to exit
    while True:
        # Play one round and update statistics
        won = guess_the_number()
        games_played += 1
        if won:
            wins += 1
        print(f"\n Games played: {games_played} | Wins: {wins}")
      
       # Replay prompt with input validation loop
        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again == "yes":
                break # Continue to the next game
            elif play_again == "no":
                # Exit the game and show final statistics
                print(f"\nFinal Score: {wins} wins out of {games_played} games played.")
                print("Thanks for playing! Goodbye!")
                return
            else:
                # Handle invalid input 
                print("Please enter 'yes' or 'no'.")
        
# Entry point - run the game
if __name__ == "__main__":
    play_game()
