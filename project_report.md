# PROJECT REPORT: CONSOLE-BASED NUMBER GUESSING GAME

**Problem Statement No.:** 89  
**Project Title:** Number Guessing Game  
**Language:** Python 3  
**Core Concepts:** Loops (`for`, `while`), Conditional Branching (`if-elif-else`), Modular Functions, Exception Handling (`try-except`), `random` Module, Global State Tracking

---

## 1. Abstract & Problem Definition

The **Number Guessing Game** is an interactive, console-based application developed in Python 3. The core objective of the problem statement is to build a program where the computer selects a secret integer between `1` and `100` and challenges the player to deduce the number within a strict limit of `5` attempts, providing directional feedback (`"Too high!"` or `"Too low!"`) after each incorrect guess.

To demonstrate structured software design and defensive programming, this implementation extends the base requirement into a **progressive 5-level game** with carryover lifelines, input validation against invalid data types and out-of-bounds numbers, a deterministic `TEST_MODE` switch for verification, and persistent session high-score tracking.

---

## 2. System Architecture & Control Flow

The application follows a top-down modular architecture where each responsibility is isolated into a dedicated function:

```text
main()
 └── while True: (Session Replay Loop)
      └── play_game()
           ├── show_guidelines()
           ├── generate_secret_number()  --> Checks TEST_MODE (42 vs random)
           └── for current_level in 1..5:  --> Progressive Level Loop
                └── while total_lifelines > 0:  --> Guess & Validation Loop
```

### Module & Function Breakdown

1. **`show_guidelines()`**
   * Displays a formatted console banner and lists the 9 gameplay rules before each session begins.
2. **`generate_secret_number()`**
   * Checks the global `TEST_MODE` flag. If `True`, returns the fixed integer `42` to allow deterministic test case verification; if `False`, calls `random.randint(1, 100)` for production gameplay.
3. **`play_game()`**
   * Orchestrates a full game session: reads and sanitizes the player's name (defaulting to `"Player"` if empty), iterates through up to 5 progressive levels, validates every guess, updates remaining lifelines, updates the global `highest_level_achieved` tracker, and prints a formatted end-of-game summary.
4. **`main()`**
   * Acts as the program entry point and manages the outer replay loop (`Play again? (y/n)`), enabling multiple consecutive sessions without restarting the script.

---

## 3. Step-by-Step Algorithmic Execution

1. **Initialization:** Set global constants `TEST_MODE = True`, `TOTAL_LEVELS = 5`, `TOTAL_LIFELINES = 5`, and initialize `highest_level_achieved = 0`.
2. **Onboarding:** Call `show_guidelines()` and prompt the user for `player_name`.
3. **Level Progression Loop (`current_level` from `1` to `5`):**
   * Verify `total_lifelines > 0`.
   * Generate `secret_number` using `generate_secret_number()`.
   * **Guessing Loop (`while total_lifelines > 0`):**
     * Prompt the user for an integer between `1` and `100`.
     * Attempt integer conversion inside a `try-except ValueError` block. If non-numeric input is entered, display an error message and `continue` without deducting a lifeline.
     * Check range boundaries (`guess < 1 or guess > 100`). If out of bounds, display a range warning and `continue` without deducting a lifeline.
     * Compare `guess` against `secret_number`:
       * **Exact Match (`guess == secret_number`):** Set `level_passed = True`, increment `levels_cleared`, congratulate the player, and `break` out of the guessing loop.
       * **Too Low (`guess < secret_number`):** Print `"Too low!"` and decrement `total_lifelines` by `1`.
       * **Too High (`guess > secret_number`):** Print `"Too high!"` and decrement `total_lifelines` by `1`.
   * **Failure Check:** If `level_passed` is `False`, print the Game Over message, reveal `secret_number`, set `game_over = True`, and `break` out of the level loop.
   * **Record Update:** If `current_level > highest_level_achieved`, update `highest_level_achieved`.
4. **Game Summary:** Print the final summary table showing `Player Name`, `Total Levels Cleared`, `Highest Level Record`, `Lifelines Left`, and final `Result` (`VICTORY!` or `GAME OVER!`).
5. **Replay Prompt:** Ask `Play again? (y/n)`. If `'y'`, start a new game; otherwise, exit gracefully.

---

## 4. Test Cases & Verification Matrix

All mandatory test cases from Problem Statement No. 89 were executed with `TEST_MODE = True` (Secret Number = `42`):

| Test Case | Test Scenario | Input Sequence | Expected Behavior | Actual Output / Behavior | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC 1** | Normal Input (Immediate Win) | `42` | Recognizes exact match on the first guess and clears the level without losing lifelines. | Cleared Level 1 immediately; `5` lifelines remaining. | **Pass** |
| **TC 2** | Boundary / Limit Inputs | `1`, then `100` | Accepts range limits (`1` and `100`), prints `"Too low!"` and `"Too high!"`, and deducts 1 lifeline per guess. | `1` $\rightarrow$ `"Too low!"` (`4` left)<br>`100` $\rightarrow$ `"Too high!"` (`3` left) | **Pass** |
| **TC 3** | Invalid Inputs (Type & Range) | `abc`, then `150` | Rejects non-integer strings and out-of-range numbers without deducting any lifelines. | Printed error prompts for both; lifelines remained `5`. | **Pass** |
| **TC 4** | Exhausted Lifelines (Loss) | `10, 90, 50, 30, 20` | Outputs directional hints in sequence, ends game when lifelines reach `0`, and reveals `42`. | Printed `Too low`, `Too high`, `Too high`, `Too low`, `Too low`; ended game and revealed `42`. | **Pass** |

---

## 5. Complete Console Dry Run Traces

### Dry Run A: Validation & Exhausted Lifelines (Test Cases 3 & 4)

```text
============================================================
                WELCOME TO 'GUESS THE NUMBER'                 
============================================================
GAME GUIDELINES:
1. There are 5 progressive levels in this game.
2. In each level, the computer picks a number between 1 and 100.
3. You have only 5 TOTAL lifelines for the entire game.
4. Incorrect guesses deduct 1 lifeline.
5. Lifelines carry over across all 5 levels.
6. You will receive 'Too high' or 'Too low' hints.
7. Guess correctly to clear a level and advance.
8. Invalid inputs do not consume a lifeline.
9. If all lifelines are used, the game ends immediately.
============================================================

Enter your name to start playing: Sujal

Hello, Sujal! Let's begin the game. Good luck!


==================== LEVEL 1 ====================
Lifelines available: 5

Lifelines remaining: 5
[Sujal] Guess a number between 1 and 100: abc
Invalid input. Enter a whole number.

Lifelines remaining: 5
[Sujal] Guess a number between 1 and 100: 150
Out of range. Enter a number between 1 and 100.

Lifelines remaining: 5
[Sujal] Guess a number between 1 and 100: 10
Too low!
Lifelines left: 4

Lifelines remaining: 4
[Sujal] Guess a number between 1 and 100: 90
Too high!
Lifelines left: 3

Lifelines remaining: 3
[Sujal] Guess a number between 1 and 100: 50
Too high!
Lifelines left: 2

Lifelines remaining: 2
[Sujal] Guess a number between 1 and 100: 30
Too low!
Lifelines left: 1

Lifelines remaining: 1
[Sujal] Guess a number between 1 and 100: 20
Too low!
Lifelines left: 0

Game Over! You ran out of lifelines on Level 1.
The secret number was: 42

============================================================
                      GAME SUMMARY                      
============================================================
Player Name: Sujal
Total Levels Cleared: 0 out of 5
Highest Level Record: Level 0
Lifelines Left: 0
Result: GAME OVER!
============================================================

Play again? (y/n): n

Thanks for playing 'Guess The Number'! Goodbye!
```

### Dry Run B: Boundary Checks & Multi-Level Victory (Test Cases 1 & 2)

```text
==================== LEVEL 1 ====================
Lifelines available: 5

Lifelines remaining: 5
[Sujal] Guess a number between 1 and 100: 1
Too low!
Lifelines left: 4

Lifelines remaining: 4
[Sujal] Guess a number between 1 and 100: 100
Too high!
Lifelines left: 3

Lifelines remaining: 3
[Sujal] Guess a number between 1 and 100: 42

Congratulations! You cleared Level 1!
Lifelines remaining: 3

Well done! Get ready for Level 2.

==================== LEVEL 2 ====================
Lifelines available: 3

Lifelines remaining: 3
[Sujal] Guess a number between 1 and 100: 42

Congratulations! You cleared Level 2!
Lifelines remaining: 3

Well done! Get ready for Level 3.
...
(Levels 3, 4, and 5 cleared with guess 42)
...
AMAZING! You completed all 5 levels!
You are the ultimate Number Guessing Champion!

============================================================
                      GAME SUMMARY                      
============================================================
Player Name: Sujal
Total Levels Cleared: 5 out of 5
Highest Level Record: Level 5
Lifelines Left: 3
Result: VICTORY!
============================================================

Play again? (y/n): n

Thanks for playing 'Guess The Number'! Goodbye!
```

---

## 6. Conclusion

The Number Guessing Game successfully meets the functional objectives of Problem Statement No. 89 while demonstrating clean modular design, nested control structures, exception-based input validation, and thorough test coverage. Switching `TEST_MODE` between `True` and `False` allows seamless transitions between deterministic evaluation and live randomized gameplay.
