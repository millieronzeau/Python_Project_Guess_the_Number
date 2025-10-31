#  Import the random module to generate a random number
import random

# Difficulty level game settings 
difficulty_levels = {
    "easy":(15, (1,50)),
    "medium":(10, (1,100)),
    "hard":(10, (1,200))
}

def select_difficulty():
    """ Prompts the user to select a difficulty level.
    Returns the corresponding max attempts and number range.
    """
    print("Choose a Difficulty Level: easy / medium / hard")
    while True:
        select = input("Enter difficulty: ").strip().lower()
        if select in difficulty_levels:
            max_attempts, number_range = difficulty_levels[select]
            print(f"You selected '{select}' difficulty: {max_attempts} attempts, number range {number_range[0]} to {number_range[1]}.")
            return max_attempts, number_range
        else:
            print("Invalid choice. Please select easy / medium / hard")

def change_difficulty():
    """ Prompts the user to change difficulty level.
    Returns True if the user wants to change, False otherwise.
    """
    while True:
        change = input("Do you want to change the difficulty level for the next round? (yes/no): ").strip().lower()
        if change == "yes":
            return True
        elif change == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def guess_the_number(max_attempts, number_range): 
    """ Runs one round of the 'Guess the Number' game.
    Accepts maximum attempts and number range as parameters.
    Prompts the player to guess, provides feedback and tracks attempts.
    Returns True if the player wins, False otherwise.
    """
    # Generate a random number between 1 and 100
    number = random.randint(*number_range)
    attempts = 0

    # Round introduction
    print(f"\nI am thinking of a number between {number_range[0]} and {number_range[1]}.")
    print(f"You have {max_attempts} attempts to guess the number.")

    # Loop until the user guesses the correct number or runs out of attempts
    while attempts < max_attempts:
        try:
            # Show current attempt number 
            print(f"\nAttempt {attempts + 1} of {max_attempts}")
            
            # Get user input
            user_guess = int(input("Enter your guess: "))

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
        
        # Validate the guess is within range
            if user_guess < number_range[0] or user_guess > number_range[1]:
                print(f"Please guess a number within the range of {number_range[0]} to {number_range[1]}.")
                continue # Skip incerementing attempts for invalid input
        # Handle non-integer inputs
        except ValueError:
            print("Please enter a valid number.")
        
    # If the user fails to guess the number within the allowed attempts
    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number}.")
        return False  # Lost score

# Replay prompt with input validation loop
def replay():
    """ Prompts the user to play again or exit.
    Returns True if the user wants to play again, False to exit."""
    while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again == "yes":
                return True
            elif play_again == "no":
                return False
            else:
                # Handle invalid input 
                print("Please enter 'yes' or 'no'.")

def play_game():
    """ Main loop for the 'Guess the Number' game. 
    Tracks the total games played and wins.
    Prompts the user to play again and change difficulty or exit.
    """
    print("Welcome to Guess the Number!")
    
    # Initialise counters for statistics 
    games_played = 0
    wins = 0
    difficulty = None
   # Set initial difficulty or change difficulty if returned true 
    while True:
        if difficulty == None or change_difficulty():
           difficulty = select_difficulty()
        
        max_attempts, number_range = difficulty
        won = guess_the_number(max_attempts= max_attempts, number_range=number_range)
        games_played += 1
        if won:
            wins += 1
        print(f"\n Games played: {games_played} | Wins: {wins}")
          # Exit the game if replay is false and show final statistics
        if not replay():
            print(f"\nFinal Score: {wins} wins out of {games_played} games played.")
            print("Thanks for playing! Goodbye!")
            break
      
# Entry point - run the game
if __name__ == "__main__":
    play_game()
