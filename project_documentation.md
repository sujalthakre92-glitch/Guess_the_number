# PROJECT DOCUMENTATION: NUMBER GUESSING GAME (PS No. 89)

## 1. Project Overview
The Number Guessing Game is a command-line console application written in Python 3. It challenges the user to guess a secret target number between 1 and 100 within a fixed pool of 5 total lifelines, providing directional hints ('Too high!' / 'Too low!') after each incorrect guess.

---

## 2. Technical Requirements & Environment
- **Language:** Python 3.x
- **Core Modules Used:** `random` (for generating random numbers in production mode)
- **Design Paradigm:** Procedural and modular programming utilizing loops, conditional statements, and exception handling.

---

## 3. Architecture & File Structure

```text
├── number_guessing_game.py   # Main Python script containing all game logic
├── README.md                 # Quick start guide and summary for GitHub
├── Project_Report.md         # Comprehensive academic report
└── DOCUMENTATION.md          # Technical documentation (this file)
```

---

## 4. Module & Function Specifications

### Global Configuration Constants
- `highest_level_achieved`: Global state variable tracking the maximum level reached across sessions.
- `TEST_MODE`: Boolean flag (`True` / `False`). When set to `True`, fixes the secret number to `42` for deterministic testing.
- `TOTAL_LEVELS`: Set to `5` to govern the progressive level loop.
- `TOTAL_LIFELINES`: Set to `5` total lifelines allocated for the entire game.

### Functions Breakdown
1. **`show_guidelines()`**
   - **Purpose:** Displays the game title banner and core rules/guidelines when the game starts.
   - **Parameters:** None
   - **Return:** None (Prints directly to stdout).

2. **`generate_secret_number()`**
   - **Purpose:** Handles secret number creation.
   - **Logic:** Checks `TEST_MODE`. Returns `42` if `True`; otherwise, returns `random.randint(1, 100)`.

3. **`play_game()`**
   - **Purpose:** Manages the primary gameplay loop, user onboarding, level progression, lifeline decrementing, input validation, and score calculation.
   - **Logic:** Iterates through 5 progressive levels, prompts the user for guesses, validates numeric input via `try-except`, and handles win/loss termination conditions.

4. **`main()`**
   - **Purpose:** Entry point of the script managing the outer replay loop.
   - **Logic:** Executes `play_game()` inside an infinite loop, prompting the user `Play again? (y/n)` upon session completion, and breaking when the user enters anything other than `'y'`.

---

## 5. Input Validation & Error Handling Strategy
- **Non-Numeric Inputs:** Caught using a `try-except ValueError` block (e.g., strings like `'abc'` or empty submissions). Prints an error message without penalizing the player's lifelines.
- **Out-of-Range Inputs:** Filtered via explicit boundary conditions (`1` to `100`) before evaluating the guess against the secret number. Prints a warning message without consuming a lifeline.

---

## 6. Setup & Execution Instructions
1. Ensure Python 3 is installed on your operating system.
2. Download or clone the project files into a local folder.
3. Open your terminal or command prompt, navigate to the folder, and run:

```bash
python number_guessing_game.py
```