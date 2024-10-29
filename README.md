** Number Guessing Game V2**

## Project Objective

This project aims to enhance a basic number guessing game by incorporating additional features to improve user experience, game functionality, and code organization. The game randomly selects a number for the player to guess, and it offers feedback after each attempt. Upgrades to the game are based on feedback and new requirements.

## Instructions

1. **Clone the Original Game Repository**
   - Start by cloning the original number guessing game repository, which includes the basic functionality outlined below:
     ```bash
     git clone https://github.dev/mushfiq-rony/number-guessing-gameV2
     ```
   = run the "main.py" file in pycharm.

2. **Original Requirements**

   The original game has the following requirements:
   - Randomly choose a number between 1 and 100 (inclusive).
   - Allow the player to input a guess.
   - Inform the player if the guess is too high, too low, or correct.
   - If the guess is incorrect, prompt the player to guess again.
   - Provide an option to quit the game at any time.
   - Reward the player for a correct guess and display the number of guesses it took.

3. **New Requirements**

   Based on the feedback, we will add new features to improve the game:

   - **Player Name**: Ask for the player's name before starting the game.
   - **Top Players Leaderboard**: After each game:
     - Update a file named `topPlayers.txt` with the player’s name and score (number of guesses).
     - Retain only the top five scores in this file.
   - **Leaderboard Display**: Display the updated top 5 players list from `topPlayers.txt`.
   - **Continuous Play Option**: Allow the player to choose to play again without restarting the program.
   - **Use Functions in a Library File**: If using multiple functions, organize them in a single library file.
   - **Error Handling**: Handle exceptions to ensure a smooth user experience.
   - **User-Friendly Design**: Create a game that is enjoyable and easy to play.

4. **Specifications for `topPlayers.txt`**

   - The file should contain up to five rows, each representing a top score.
   - Each row should include two columns:
     - **Column 1**: The score (number of guesses).
       - Starts at position 0.
     - **Column 2**: The player's name.
       - Starts at position 10.
   - Sort the file by the score column, with the lowest score at the top.

   ### Example of `topPlayers.txt`

