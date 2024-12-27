import random
from games.game_base import GameBase

class Hangman(GameBase):
    """Class for the Hangman game."""

    words = ["python", "hangman", "developer", "programming", "debugging"]

    def __init__(self):
        """Initializes the game with the name 'Hangman'."""
        super().__init__("Hangman")

    def show_instructions(self):
        """Displays the game instructions."""
        print("\n****** Welcome to Hangman! ******\n")
        print("Guess the word by suggesting one letter at a time.")
        print("You have a limited number of attempts to guess the word.")

    def play(self):
        """Executes the main game logic."""
        while True:  # Loop to allow replaying the game
            # Select a random word
            word = random.choice(self.words)
            hidden_word = ["_"] * len(word)  # Word display with blanks
            attempts_remaining = 6  # Number of wrong guesses allowed
            guessed_letters = set()

            print(f"\nThe word has {len(word)} letters: {' '.join(hidden_word)}")
            print(f"You have {attempts_remaining} attempts.")

            while attempts_remaining > 0 and "_" in hidden_word:
                print("\nGuessed letters:", " ".join(sorted(guessed_letters)))
                guess = self.get_player_guess(guessed_letters)

                if guess in word:
                    print(f"Good job! The letter '{guess}' is in the word.")
                    for i, letter in enumerate(word):
                        if letter == guess:
                            hidden_word[i] = guess
                else:
                    print(f"Wrong guess! The letter '{guess}' is not in the word.")
                    attempts_remaining -= 1

                print(f"\nCurrent word: {' '.join(hidden_word)}")
                print(f"Attempts remaining: {attempts_remaining}")

                # Check if the word is fully guessed
                if "_" not in hidden_word:
                    print("\nCongratulations! You've guessed the word!")
                    print(f"The word was: {word}")
                    break
            else:
                if "_" in hidden_word:
                    print("\nGame over! You've run out of attempts.")
                    print(f"The word was: {word}")

            # Post-game options
            choice = self.handle_post_game_options()
            if choice == "replay":
                print()
                continue
            elif choice == "change":
                break
            elif choice == "quit":
                print("\nThanks for playing! Goodbye!\n")
                exit()

    def get_player_guess(self, guessed_letters):
        """
        Gets and validates the player's guess.

        :param guessed_letters: Set of already guessed letters.
        :return: A single valid letter.
        """
        while True:
            try:
                guess = input("Enter a letter: ").lower()
                if len(guess) != 1 or not guess.isalpha():
                    raise ValueError("Please enter a single valid letter.")
                if guess in guessed_letters:
                    raise ValueError("You've already guessed that letter. Try again.")
                guessed_letters.add(guess)
                return guess
            except ValueError as e:
                print(e)
