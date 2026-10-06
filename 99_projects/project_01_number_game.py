"""
=====================================================================
PROJECT: Number Guessing Game  (Difficulty: beginner)
=====================================================================

SCENARIO
--------
Your younger cousin keeps begging you to make "a real game" together.
You agree on a classic: the computer secretly picks a number between
1 and 100 and the player has to find it. The game should nudge the
player with "too high" / "too low" hints, count every attempt, let
them give up with 'q', and offer a rematch without restarting.

WHAT YOU WILL PRACTICE
----------------------
- Variables, input() and int casting (from module 01)
- f-strings (from module 01)
- Comparison operators and if/elif/else (from module 03)
- while loops (from module 03)
- The random module (standard library, module 07 territory)

YOUR TASKS
----------
1. Write get_valid_guess(): ask for a number between 1 and 100 and
   return it as an int. If the player types 'q' (or input closes),
   return None instead.
2. If the answer is not a whole number, print a friendly hint and
   ask again (a loop is nicer than crashing).
3. If the number is outside 1-100, remind the player of the range
   and ask again.
4. Write check_guess(secret, guess): return "win", "high" or "low"
   using comparison operators.
5. Finish play_round(): loop until the player wins or quits, count
   every attempt, and print "Too high!" / "Too low!" feedback.
6. On a win, print a congratulation that includes the attempt count.
7. Write wants_to_play_again(): return True only for answers that
   start with "y".
8. Stretch: track how many rounds were won and the best (lowest)
   score across all rounds.

STARTER CODE
------------
Complete the TODOs below. Run with:
    python 99_projects/project_01_number_game.py

Hints are inline. A full solution is in answers/projects/.
=====================================================================
"""

import random

LOW = 1
HIGH = 100


def ask(prompt):
    """input() that survives closed input (pipes, redirected files)."""
    try:
        return input(prompt)
    except EOFError:
        return None


def get_valid_guess():
    """
    Ask for a number between LOW and HIGH.

    Returns the guess as an int, or None when the player quits.

    TODO 1: read a line with ask(f"Your guess (q to quit): ")
    TODO 2: if the answer is None or 'q', return None
    TODO 3: convert with int(answer) inside try/except ValueError;
            on a bad number print a hint and ask again (loop!)
    TODO 4: if the number is outside LOW..HIGH, print a reminder
            and ask again
    Hint: int("42") works, int("4x") raises ValueError.
    """
    print("TODO: implement get_valid_guess()")
    return None


def check_guess(secret, guess):
    """
    Compare the guess to the secret.

    Returns "win", "high" or "low".
    TODO: one small if/elif/else with comparison operators.
    """
    print("TODO: implement check_guess()")
    return "win"  # placeholder so the demo loop can finish


def play_round():
    """Play one round: pick a secret, count attempts, give feedback."""
    secret = random.randint(LOW, HIGH)
    attempts = 0
    print(f"\nI picked a number between {LOW} and {HIGH}. Find it!")

    while True:
        guess = get_valid_guess()
        if guess is None:
            print(f"No problem -- the secret number was {secret}.")
            return None

        attempts += 1
        result = check_guess(secret, guess)

        if result == "win":
            # TODO 6: make this message your own (mention `attempts`).
            print(f"You got it in {attempts} guess(es)!")
            return attempts
        elif result == "high":
            # TODO 5: replace these with real "too high" / "too low" text.
            print("(check_guess is still a TODO)")
        else:
            print("(check_guess is still a TODO)")


def wants_to_play_again():
    """
    TODO 7: ask "Play again? (y/n) " and return True only when the
    answer starts with 'y'. Anything else (or closed input) -> False.
    Hint: answer.strip().lower().startswith("y")
    """
    print("TODO: implement wants_to_play_again()")
    return False


def main():
    print("=" * 46)
    print("        NUMBER GUESSING GAME -- starter")
    print("  Fill in the TODOs, then come back and play!")
    print("=" * 46)

    round_number = 1
    scores = []  # stretch: store the attempts of every won round here

    playing = True
    while playing:
        result = play_round()
        if result is not None:
            scores.append(result)
        playing = wants_to_play_again()
        round_number += 1

    print("\nThanks for playing!")
    if scores:
        print(f"Rounds won: {len(scores)}, best score: {min(scores)} guess(es)")


if __name__ == "__main__":
    main()
