PROJECT DOCUMENTATION: NUMBER GUESSING GAME (PS No. 89)

1. Project Overview:
The Number Guessing Game is a command-line console application written in Python 3. It challenges the user to guess a secret target number between 1 and 100 within a fixed pool of 5 total lifelines, providing directional hints (Too high! / Too low!) after each incorrect guess.

2. Technical Requirements & Environment:
 1.Language: Python 3.x
 2.Core Modules Used: random (for generating random numbers in production mode)
 3.Design Paradigm: Procedural and modular programming utilizing loops, conditional statements, and exception handling.

3. Architecture & File Structure:
├── number_guessing_game.py   # Main Python script containing all game logic
├── README.md                 # Quick start guide and summary for GitHub
├── Project_Report.md         # Comprehensive academic report
└── DOCUMENTATION.md          # Technical documentation (this file)

4. Module & Function Specifications
Global Configuration Constants
 ->highest_level_achieved: Global state variable tracking the maximum level reached across sessions.
 ->TEST_MODE: Boolean flag (True / False).When set to True, fixes the secret number to 42 for deterministic testing.
 ->TOTAL_LEVELS: Set to 5 to govern the progressive level loop.TOTAL_LIFELINES: Set to 5 total lifelines allocated for the entire game.

Functions Breakdown
 1.show_guidelines()
   ->Purpose: Displays the game title banner and core rules/guidelines when the game starts.
   ->Parameters: None
   ->Return: None (Prints directly to stdout).

 2.generate_secret_number()
   ->Purpose: Handles secret number creation.
   ->Logic: Checks TEST_MODE. Returns 42 if True; otherwise, returns random.randint(1, 100).


