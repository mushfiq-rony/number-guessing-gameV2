import random

# Function to read and return top 5 players from the file
def read_top_players(file_name='topPlayers.txt'):
    top_players = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                score = int(line[:10].strip())  # First 10 characters for score
                name = line[10:].strip()  # Rest of the line is the player's name
                top_players.append((score, name))  # Store as (score, name)
        # Sort players by score (ascending)
        top_players.sort(key=lambda x: x[0])
    except FileNotFoundError:
        print(f"No previous records found. {file_name} will be created.")
    return top_players[:5]  # Return only the top 5 players


# Function to update the top 5 players in the file
def update_top_players(player_name, score, file_name='topPlayers.txt'):
    # Read existing players
    top_players = read_top_players(file_name)
    # Append the new player's score and name
    top_players.append((score, player_name))
    # Sort by score (ascending order)
    top_players.sort(key=lambda x: x[0])
    # Keep only top 5
    top_players = top_players[:5]

    # Write the updated top 5 back to the file
    with open(file_name, 'w') as file:
        for i, player in enumerate(top_players):
            # Write each line with the name left-aligned and score after it
            file.write(f"{str(player[0]).ljust(10)}{player[1]}")

            # Add a newline if it’s not the last player
            if i < len(top_players) - 1:
                file.write("\n")


# Function to display top players
def display_top_players(file_name='topPlayers.txt'):
    top_players = read_top_players(file_name)
    if top_players:
        print("\nTop 5 Players:")
        for i, player in enumerate(top_players, 1):
            print(f"{i}. {player[0]} guesses for - {player[1]}")
    else:
        print("No top players yet.")


# Main game loop
def play_game():
    player_name = input("What's your name? (Enter your name): ")  # Ask for player's name


    while True:
        correct_number = random.randint(1, 100) # select a random number between 1 and 100
        guess_count = 0 # number of guess counting 
        print(f"Hi {player_name}, welcome to the guessing game!")
        print("\nI have picked a number between 1 and 100. Try to guess it!")
        print("You can type 'q' to quit at any time.")

        while True:
            guess = input("What's your guess? (1-100, or 'q/Q' to quit): ") # input of the player name

            # Quit if the player enters 'q'
            if guess.lower() == 'q':
                print(f"Thanks for playing, {player_name}. See you next time!")
                return  # Exit the game loop

            # Check if the input is a valid digit and within range of 1 and 100
            if guess.isdigit() and 1 <= int(guess) <= 100:
                guess = int(guess)  # Convert guess to integer
                guess_count += 1

                # starting the conditions of the game
                if guess < correct_number:
                    print("Wrong. Guess higher!")
                elif guess > correct_number:
                    print("Wrong. Guess lower!")
                else:
                    print(f"Congrats, {player_name}! You guessed the number {correct_number} in {guess_count} guesses.")
                    update_top_players(player_name, guess_count)
                    display_top_players()
                    break  # End the current game and ask to replay
            else:
                print("Invalid input: Please guess a number between 1 and 100.")

        # Ask if the player wants to play again
        while True:
            play_again = input("Do you want to play again? (yes/y or no/n): ").lower()

            # Check if the player wants to play again
            if play_again in ['yes', 'y']:
                # Ask if the player is the same or a new one
                same_player = input("Are you the same player? (yes/y for same, no/n for new): ").lower()
                if same_player in ['no', 'n']:
                    player_name = input("What's your name? (Enter your name) ")
                break  # Exit the input validation loop and start a new game
            elif play_again in ['no', 'n']:
                print(f"Goodbye, {player_name}!")
                return  # Exit the game entirely
            else:
                # Invalid input, repeat the loop until a valid answer is given
                print("Invalid input. Please type 'yes/y' or 'no/n'.")
