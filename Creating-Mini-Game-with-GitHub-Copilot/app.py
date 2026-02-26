"""
Rock, Paper, Scissors Game

This is a classic rock-paper-scissors game where the player competes against the computer.

Game Rules:
    - Rock beats Scissors
    - Scissors beats Paper
    - Paper beats Rock

Features:
    - Computer randomly chooses rock, paper, or scissors
    - Player input validation with error warnings
    - Round results (win, lose, or tie)
    - Score tracking throughout the game
    - Replay option after each round
    - Final score display with wins and total rounds

Implementation Details:
    - All player inputs are converted to lowercase for comparison
    - Game continues until player chooses to stop
"""

import random

# Initialize game variables
player_score = 0
total_rounds = 0
play_again = True

while play_again:
    # Get player input (automatically converted to lowercase)
    player_choice = input("\nEnter rock, paper, or scissors: ").lower()
    
    # Validate player input - check if valid option and warn if invalid
    valid_options = ["rock", "paper", "scissors"]
    if player_choice not in valid_options:
        print("Invalid option! Please enter rock, paper, or scissors.")
        continue
    
    # Computer randomly chooses from available options
    computer_choice = random.choice(valid_options)
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Compare choices and determine winner, then update score
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You won!")
        player_score += 1
    else:
        print("You lost!")
    
    # Increment total rounds played
    total_rounds += 1
    
    # Ask player if they want to play another round
    while True:
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input in ["yes", "no"]:
            play_again = play_again_input == "yes"
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

# Display final score and game statistics
print(f"\n{'='*50}")
print(f"Game Over! Final Score: {player_score} wins out of {total_rounds} rounds")
print(f"{'='*50}")
