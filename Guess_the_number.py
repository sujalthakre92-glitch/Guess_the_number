import random

# Global variable to store the highest level achieved across sessions
highest_level_achieved = 0

def show_guidelines():
    """Displays the title and game guidelines."""
    print("=" * 60)
    print("                 WELCOME TO 'GUESS THE NUMBER'                 ")
    print("=" * 60)
    print("GAME GUIDELINES:")
    print("1. There are 5 progressive levels in this game.")
    print("2. In each level, the computer picks a secret number between 1 and 100.")
    print("3. You have 5 TOTAL lifelines (attempts) for the ENTIRE game.")
    print("4. Incorrect guesses deduct 1 lifeline. Lifelines carry over across levels.")
    print("5. You will receive 'Too high' or 'Too low' hints after each incorrect guess.")
    print("6. Guess correctly to clear a level and advance to the next.")
    print("7. If you run out of all 5 lifelines at any point, the game ends immediately.")
    print("=" * 60)

def play_game():
    global highest_level_achieved
    show_guidelines()

    # Get player name
    player_name = input("\nEnter your name to start playing: ").strip()
    if not player_name:
        player_name = "Player"
        
    print(f"\nHello, {player_name}! Let's begin the game. Good luck!\n")
    
    total_levels = 5
    levels_cleared = 0
    total_lifelines = 5  # Shared lifeline pool across all 5 levels
    
    # Loop through each level
    for current_level in range(1, total_levels + 1):
        if total_lifelines <= 0:
            break
            
        print(f"\n--- LEVEL {current_level} of {total_levels} ---")
        secret_number = random.randint(1, 100)
        level_passed = False
        
        while total_lifelines > 0:
            print(f"Lifelines remaining for the game: {total_lifelines}")
            user_input = input(f"[{player_name}] Guess a number between 1 and 100: ").strip()
            
            # Input validation: Check if input is a valid integer
            if not user_input.isdigit():
                print("Invalid input. Enter a whole number.")
                continue
                
            guess = int(user_input)
            
            # Input validation: Check if number is within range (1 to 100)
            if guess < 1 or guess > 100:
                print("Out of range. Enter a number between 1 and 100.")
                continue
                
            # Check the guess
            if guess == secret_number:
                print(f"Congratulations! You cleared Level {current_level}!")
                level_passed = True
                levels_cleared += 1
                break
            elif guess < secret_number:
                print("Too low!")
                total_lifelines -= 1
            else:
                print("Too high!")
                total_lifelines -= 1
                
        # If player ran out of lifelines
        if not level_passed and total_lifelines <= 0:
            print(f"\nGame Over! You ran-out of lifelines on Level {current_level}.")
            print(f"The secret number was: {secret_number}")
            break

    # Update global high score record
    if levels_cleared > highest_level_achieved:
        highest_level_achieved = levels_cleared
        print(f"\n NEW HIGH SCORE! You achieved a new personal best of Level {highest_level_achieved}!")

    # Final Summary
    print("\n" + "=" * 60)
    print("                      GAME SUMMARY                      ")
    print("=" * 60)
    print(f"Player Name: {player_name}")
    print(f"Total Levels Cleared: {levels_cleared} out of {total_levels}")
    print(f"Highest Level Record: Level {highest_level_achieved}")
    print(f"Lifelines Left: {total_lifelines}")
    if levels_cleared == total_levels:
        print("Incredible job! You cleared all 5 levels!")
    print("=" * 60)

def main():
    while True:
        play_game()
        replay = input("\nPlay again? (y/n): ").strip().lower()
        if replay != 'y':
            print("\nThanks for playing 'Guess The Number'! Goodbye!")
            break

if __name__ == "__main__":
    main()