
import random

# Global variable to store the highest level achieved across sessions
highest_level_achieved = 0

# Game configuration
TEST_MODE = True  # Set to True for testing, False for production
TOTAL_LEVELS = 5
TOTAL_LIFELINES = 5


def show_guidelines():
    """Displays the title and game guidelines."""

    print("=" * 60)
    print("                 WELCOME TO 'GUESS THE NUMBER'                 ")
    print("=" * 60)
    print("GAME GUIDELINES:")
    print("1. There are 5 progressive levels in this game.")
    print("2. In each level, the computer picks a number between 1 and 100.")
    print("3. You have only 5 TOTAL lifelines for the entire game.")
    print("4. Incorrect guesses deduct 1 lifeline.")
    print("5. Lifelines carry over across all 5 levels.")
    print("6. You will receive 'Too high' or 'Too low' hints.")
    print("7. Guess correctly to clear a level and advance.")
    print("8. Invalid inputs do not consume a lifeline.")
    print("9. If all lifelines are used, the game ends immediately.")
    print("=" * 60)


def generate_secret_number():
    """Generates the secret number."""

    if TEST_MODE:
        return 42
    else:
        return random.randint(1, 100)


def play_game():
    global highest_level_achieved

    show_guidelines()

    # Get player name
    player_name = input("\nEnter your name to start playing: ").strip()

    if not player_name:
        player_name = "Player"

    print(f"\nHello, {player_name}! Let's begin the game. Good luck!\n")

    # Initialize game variables
    total_lifelines = TOTAL_LIFELINES
    levels_cleared = 0
    game_over = False

    # Loop through all five progressive levels
    for current_level in range(1, TOTAL_LEVELS + 1):

        if total_lifelines <= 0:
            break

        print(f"\n{'=' * 20} LEVEL {current_level} {'=' * 20}")
        print(f"Lifelines available: {total_lifelines}")

        secret_number = generate_secret_number()
        level_passed = False

        # Continue guessing while lifelines are available
        while total_lifelines > 0:

            print(f"\nLifelines remaining: {total_lifelines}")

            user_input = input(
                f"[{player_name}] Guess a number between 1 and 100: "
            ).strip()

            # Validate numeric input
            try:
                guess = int(user_input)

            except ValueError:
                print("Invalid input. Enter a whole number.")
                continue

            # Validate number range
            if guess < 1 or guess > 100:
                print("Out of range. Enter a number between 1 and 100.")
                continue

            # Check the guess
            if guess == secret_number:

                level_passed = True
                levels_cleared += 1

                print(
                    f"\nCongratulations! You cleared Level {current_level}!"
                )

                print(f"Lifelines remaining: {total_lifelines}")

                break

            elif guess < secret_number:

                print("Too low!")
                total_lifelines -= 1

            else:

                print("Too high!")
                total_lifelines -= 1

            # Display remaining lifelines
            print(f"Lifelines left: {total_lifelines}")

        # Check whether the player failed the level
        if not level_passed:

            print(
                f"\nGame Over! You ran out of lifelines "
                f"on Level {current_level}."
            )

            print(f"The secret number was: {secret_number}")

            game_over = True
            break

        # Update highest level achieved
        if current_level > highest_level_achieved:
            highest_level_achieved = current_level

        # Prepare for next level
        if current_level < TOTAL_LEVELS:

            print(
                f"\nWell done! Get ready for Level {current_level + 1}."
            )

    # Display final victory message
    if not game_over and levels_cleared == TOTAL_LEVELS:

        print("\nAMAZING! You completed all 5 levels!")
        print("You are the ultimate Number Guessing Champion!")

    # Final game summary
    print("\n" + "=" * 60)
    print("                      GAME SUMMARY                      ")
    print("=" * 60)

    print(f"Player Name: {player_name}")
    print(f"Total Levels Cleared: {levels_cleared} out of {TOTAL_LEVELS}")
    print(f"Highest Level Record: Level {highest_level_achieved}")
    print(f"Lifelines Left: {total_lifelines}")

    if not game_over and levels_cleared == TOTAL_LEVELS:
        print("Result: VICTORY!")
    else:
        print("Result: GAME OVER!")

    print("=" * 60)


def main():
    """Main function with replay functionality."""

    while True:

        play_game()

        replay = input("\nPlay again? (y/n): ").strip().lower()

        if replay != 'y':

            print("\nThanks for playing 'Guess The Number'! Goodbye!")
            break


if __name__ == "__main__":
    main()



