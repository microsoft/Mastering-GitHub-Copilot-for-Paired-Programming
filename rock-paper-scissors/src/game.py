print("Welcome to Rock-Paper-Scissors!")
import random
from utils import get_user_choice, display_choices, display_result
from logic import get_computer_choice, determine_winner

def main():
    player_score = 0
    rounds = 0

    while True:
        player_choice = get_user_choice()
        computer_choice = get_computer_choice()
        display_choices(player_choice, computer_choice)

        result = determine_winner(player_choice, computer_choice)
        display_result(result)

        if result == "win":
            player_score += 1

        rounds += 1
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

    print(f"Game over! You won {player_score} out of {rounds} rounds.")

if __name__ == "__main__":
    main()