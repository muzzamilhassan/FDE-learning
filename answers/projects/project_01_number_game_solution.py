"""
Solution for Project 01 - Number Guessing Game.

Run it with:
    python answers/projects/project_01_number_game_solution.py

Try to finish the starter in 99_projects/ on your own first,
then compare your version with this one. Different is fine --
if it plays, you won.
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
    """Ask until the player enters a whole number in range, or quits."""
    while True:
        answer = ask(f"Your guess ({LOW}-{HIGH}, q to quit): ")
        if answer is None or answer.strip().lower() == "q":
            return None
        answer = answer.strip()
        if not answer.lstrip("-").isdigit():
            print(f"  '{answer}' is not a whole number. Try again!")
            continue
        guess = int(answer)
        if LOW <= guess <= HIGH:
            return guess
        print(f"  {guess} is outside {LOW}-{HIGH}. Try again!")


def check_guess(secret, guess):
    """Return 'win', 'high' or 'low'."""
    if guess == secret:
        return "win"
    if guess > secret:
        return "high"
    return "low"


def play_round(round_number):
    """Play one round. Returns the attempt count, or None on quit."""
    secret = random.randint(LOW, HIGH)
    attempts = 0
    print(f"\n--- Round {round_number}: I am thinking of a number "
          f"between {LOW} and {HIGH}... ---")

    while True:
        guess = get_valid_guess()
        if guess is None:
            print(f"  No problem! The secret number was {secret}.")
            return None

        attempts += 1
        result = check_guess(secret, guess)

        if result == "win":
            print(f"  Correct! You found {secret} in {attempts} guess(es).")
            return attempts
        if result == "high":
            print("  Too high -- go lower.")
        else:
            print("  Too low -- go higher.")


def wants_to_play_again():
    """True only for answers starting with 'y'."""
    answer = ask("\nPlay again? (y/n): ")
    return bool(answer) and answer.strip().lower().startswith("y")


def main():
    print("=" * 46)
    print("           NUMBER GUESSING GAME")
    print(f"   Find my secret number between {LOW} and {HIGH}!")
    print("=" * 46)

    round_number = 1
    scores = []  # attempts of every round the player actually won

    while True:
        attempts = play_round(round_number)
        if attempts is not None:
            scores.append(attempts)
        if not wants_to_play_again():
            break
        round_number += 1

    print("\nThanks for playing!")
    if scores:
        print(f"  Rounds won : {len(scores)}")
        print(f"  Best score : {min(scores)} guess(es)")
        print(f"  Average    : {sum(scores) / len(scores):.1f} guess(es)")
    print("Goodbye!")


if __name__ == "__main__":
    main()
