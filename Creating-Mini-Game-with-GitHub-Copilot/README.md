# Creating a Mini Game with GitHub Copilot

In this module, you'll use GitHub Copilot to build a classic rock, paper, scissors game in Python. This hands-on exercise will help you practice prompt-driven development, strengthen your Python skills, and learn how GitHub Copilot can support you as a paired programming partner.

- **Who this is for**: Developers, DevOps engineers, software development managers, and testers
- **What you'll learn**: How to use GitHub Copilot to generate, refine, and explain Python code
- **What you'll build**: A Python console-based rock, paper, scissors minigame
- **Prerequisites**: A GitHub account with access to GitHub Copilot
- **Timing**: About 1 hour

By the end of this module, you'll be able to:

- Use GitHub Codespaces as a development environment
- Build input and output flows in a Python console application
- Work with GitHub Copilot as a coding assistant

## Before you begin

We recommend reviewing these resources before starting:

- [Introduction to prompt engineering with GitHub Copilot](https://learn.microsoft.com/training/modules/introduction-prompt-engineering-with-github-copilot/?WT.mc_id=academic-113596-abartolo)
- [Challenge project - Build a minigame with GitHub Copilot and Python](https://learn.microsoft.com/training/modules/challenge-project-create-mini-game-with-copilot/?WT.mc_id=academic-113596-abartolo)
- [Learn Live: Build a minigame console app with GitHub Copilot](https://youtu.be/Fi_jl3G7i8Y?si=v56VPYfTHYBBEX11)

## Requirements

- Enable your [GitHub Copilot service](https://github.com/github-copilot/signup)

## Exercise

**Right-click the "Open in GitHub Codespaces" button to open your Codespace in a new tab.**

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)

In this exercise, you'll build a Python minigame with GitHub Copilot in GitHub Codespaces.

## Step 1: Verify your Codespace setup

1. Open your Codespace for this repository.
2. In Visual Studio Code, create a new file named `app.py`.

   **Note:** If Python support is not already available in your environment, install the Python extension for Visual Studio Code.

3. In `app.py`, type the following comment:

   ```python
   # write "hello world" to the console
   ```

4. Let GitHub Copilot suggest the implementation. You should see something similar to:

   ```python
   # write "hello world" to the console
   print("hello world")
   ```

5. Run the application in the terminal:

   ```bash
   python app.py
   ```

6. Confirm that the output is similar to:

   ```bash
   hello world
   ```

If this works, your Codespace and GitHub Copilot are ready.

## Step 2: Build the game logic

Now that you've confirmed GitHub Copilot is working, use it to help you build a rock, paper, scissors game in Python.

### Game rules

The winner of each round is determined by these rules:

- **Rock** beats **scissors**
- **Scissors** beats **paper**
- **Paper** beats **rock**

### Game requirements

Your program should:

- Allow the computer to randomly choose `rock`, `paper`, or `scissors`
- Ask the player to enter `rock`, `paper`, or `scissors`
- Convert player input to lowercase before checking it
- Warn the player if they enter an invalid option
- Tell the player whether they won, lost, or tied each round
- Ask the player if they want to play another round
- Display the player's score when the game ends

## Step 3: Use Copilot to build the game incrementally

A good way to work with GitHub Copilot is to build the program in small steps. Try adding comments like these to guide Copilot:

```python
# import the random module

# define the valid options: rock, paper, scissors

# ask the player to choose rock, paper, or scissors

# convert the player's input to lowercase

# validate the player's input and show an error message if it is invalid

# randomly select rock, paper, or scissors for the computer

# compare the player choice with the computer choice

# print whether the player won, lost, or tied

# ask the player if they want to play again

# keep track of total rounds and total wins

# print the final score when the game ends
```

As you work, review Copilot's suggestions carefully. You can accept, reject, or edit them to improve the code.

## Step 4: Example interaction

Your finished program might behave like this:

```text
Choose rock, paper, or scissors: rock
Computer chose: scissors
You win!

Play again? (y/n): y
Choose rock, paper, or scissors: screen
Invalid option. Please choose rock, paper, or scissors.

Choose rock, paper, or scissors: paper
Computer chose: rock
You win!

Play again? (y/n): n
Final score: 2 wins out of 2 rounds.
```

## Step 5: Verify your work

Run the game with:

```bash
python app.py
```

Then confirm that your game does all of the following:

- Accepts `rock`, `paper`, or `scissors` as valid input
- Rejects invalid input such as `screen`
- Converts user input to lowercase before evaluation
- Randomly selects a choice for the computer
- Correctly reports win, loss, or tie results
- Lets the player continue playing multiple rounds
- Displays the number of wins and rounds played at the end

## Tips for working with GitHub Copilot

- Write clear comments before asking Copilot for suggestions
- Build one small feature at a time
- Test your program after each change
- Edit Copilot's suggestions when needed instead of accepting everything as-is
- Use Copilot as a collaborator, not a replacement for your own review

## Conclusion

Congratulations on completing this challenge exercise! You've created a Python console minigame and practiced using GitHub Copilot to plan, generate, and refine code in an iterative way.
