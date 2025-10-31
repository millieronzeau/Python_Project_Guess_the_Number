# Python_Project_Guess_the_Number
## Guess The Number Game 

A fun and interactive **number guessing game** built with Python!  
Test your guessing skills across multiple difficulty levels and track your wins over multiple rounds.

---

## Game Overview

The computer will randomly select a number within a given range based on the chosen difficulty level.  
Your goal is to **guess the correct number** within a limited number of attempts.  

You’ll receive feedback after each guess to help narrow down your options.

---

## Features

Three difficulty levels:
- **Easy:** 15 attempts, range 1–50  
- **Medium:** 10 attempts, range 1–100  
- **Hard:** 10 attempts, range 1–200  

Smart input validation - prevents crashes on invalid entries  
Option to change difficulty after each round  
Tracks total games played and wins  
Fully text-based interface 

---

## Requirements

Before you begin, ensure you have:

- **Python 3.8+** installed  

You can use **any text editor or IDE** (VS Code instructions below) to run this game.

No third-party libraries are required - only the built-in `random` module is used.

---

## How to Run the Game in VS Code

1. **Save the script** as `guess_the_number.py` in your game folder.
2. **Open the folder** in VS Code.
3. **Run the python file** (play button at top right)
4. Follow the on-screen prompts to play!

---

## How to Play

1. A welcome statement will be shown
2. When prompted, **choose a difficulty level** (`easy`, `medium`, or `hard`).
3. Try to **guess the number** within the given attempts.
4. After each guess, the game will tell you if your guess was:
   - Too high   
   - Too low   
   - Correct   
5. You win by guessing the correctly within the given attempts.
6. After a round:
   - Choose whether to **play again**.  
   - Optionally **change difficulty** before the next round.
7. Your score and number of rounds played will be tracked!

---

## Example Gameplay

```
Welcome to Guess the Number!
Select Difficulty Level: easy / medium / hard
Select difficulty: medium
You selected 'medium' difficulty: 10 attempts, number range 1 to 100.

I am thinking of a number between 1 and 100.
You have 10 attempts to guess the number.

Attempt 1 of 10
Enter your guess: 50
Too low! Try again.

Attempt 2 of 10
Enter your guess: 75
Too high! Try again.

Attempt 3 of 10
Enter your guess: 63
Congratulations! You've guessed the number 63 in 3 attempts.

Games played: 1 | Wins: 1
Do you want to play again? (yes/no): no

Final Score: 1 wins out of 1 games played.
Thanks for playing! Goodbye!
```

---
## Flowchart Overview

The game logic is visually mapped in flowchart.pdf. 
It provides a clear view of the program’s control flow, including:

- Game Start
- Difficulty selection  
- Random number generation  
- Guessing loop with feedback  
- Win/loss conditions  
- Replay decision and loopback including changing difficultya
- Score and rounds played tracking

To view the flowchart:
- Open the PDF directly from the repository
---

## File Structure

```
guess_the_number/
│
├── guess_the_number.py       # Main Python game script
├── README.md                 # Game documentation (this file)
└── flowchart.pdf             # Visual flowchart of game logic (PDF format)
```

---

##  Tips

- You can edit the `difficulty_levels` dictionary at the top of the script to customize your own difficulty settings.
- Try increasing the range or lowering attempts for an extra challenge!


