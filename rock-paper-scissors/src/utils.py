def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    return choice

def display_choices(player_choice, computer_choice):
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

def display_result(result):
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("It's a tie!")