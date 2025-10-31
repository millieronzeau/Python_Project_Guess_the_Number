#  Import the random module to generate a random number 
import random

# Difficulty level settings 
DIFFICULTY_LEVELS = {
    "easy":(15, (1,50)),
    "medium":(10, (1,100)),
    "hard":(5, (1,100))
}

def set_difficulty() -> tuple[int, tuple[int, int]]:
    """ Prompts the user to select a difficulty level.
    Returns the corresponding max attempts and number range.
    """
    print("Select Difficulty Level: easy / medium / hard")
    while True:
        choice = input("Enter difficulty: ").strip().lower()
        if choice in DIFFICULTY_LEVELS:
            max_attempts, number_range = DIFFICULTY_LEVELS[choice]
            print(f"You selected '{choice}' difficulty: {max_attempts} attempts, number range {number_range[0]} to {number_range[1]}.")
            return max_attempts, number_range
        else:
            print("Invalid choice. Please select easy / medium / hard")

def prompt__change_difficulty() -> bool:
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



def guess_the_number(max_attempts: int, number_range: tuple[int, int]) -> bool:
    """ Runs one round of the 'Guess the Number' game.
    Accepts maximum attempts and number range as parameters.
    Prompts the player to guess, provides feedback and tracks attempts.
    Returns True if the player wins, False otherwise.
    """

    # Generate a random number between 1 and 100
    number = random.randint(*number_range)
    attempts = 0

    # Game introduction
    print(f"\nI am thinking of a number between {number_range[0]} and {number_range[1]}.")
    print(f"You have {max_attempts} attempts to guess the number.")

    # Loop until the user guesses the correct number or runs out of attempts
    while attempts < max_attempts:
        try:
            # Show current attempt number 
            print(f"\nAttempt {attempts + 1} of {max_attempts}")
            
            # Get user input
            user_guess = int(input("Enter your guess: "))
           
            # Validate the guess is within range
            if user_guess < number_range[0] or user_guess > number_range[1]:
                print(f"Please guess a number within the range of {number_range[0]} to {number_range[1]}.")
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

# Replay prompt with input validation loop
def prompt_replay() -> bool:
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
    Prompts the user to play again or exit.
    """
    print("Welcome to Guess the Number!")
    # Initialise counters for statistics 
    games_played = 0
    wins = 0
    current_difficulty = None
   
    while True:
        if current_difficulty==None or prompt__change_difficulty():
            current_difficulty = set_difficulty()
        
        max_attempts, number_range = current_difficulty
        won = guess_the_number(max_attempts= max_attempts, number_range=number_range)
        games_played += 1
        if won:
            wins += 1
        print(f"\n Games played: {games_played} | Wins: {wins}")
          # Exit the game and show final statistics
        if not prompt_replay():
            print(f"\nFinal Score: {wins} wins out of {games_played} games played.")
            print("Thanks for playing! Goodbye!")
            break
      
# Entry point - run the game
if __name__ == "__main__":
    play_game()
