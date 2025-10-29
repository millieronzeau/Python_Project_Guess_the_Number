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
            # Get user input
            user_guess = int(input("Enter your guess: "))
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
        except ValueError:
            print("Please enter a valid integer.")
        
    # If the user fails to guess the number within the allowed attempts
    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number}.")
        # Lose score
        return False 

# Function to play the game again
def play_game():
    print("Welcome to 'Guess the Number'!")
    games_played = 0
    wins = 0
    
    while True:
        won = guess_the_number()
        games_played += 1
        if won:
            wins += 1
        
        print(f"\n Games played: {games_played} | Wins: {wins}")
       
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print(f"\nFinal Score: {wins} wins out of {games_played} games played.")
            print("Thanks for playing! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
