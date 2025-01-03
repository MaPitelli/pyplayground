import random
from games.game_base import GameBase

class RockPaperScissors(GameBase):
    """Class for the Rock, Paper, Scissors game."""

    options = ["Rock", "Paper", "Scissors"]

    def __init__(self):
        """Initializes the game with the name 'Rock, Paper, Scissors'."""
        super().__init__("Rock, Paper, Scissors")

    def play(self):
        """Executes the main game logic."""
        while True:  # Loop to allow replaying the game
            player_choice = self.get_player_choice()
            computer_choice = random.choice(self.options)

            print(f"\nThe computer chose: {computer_choice}\n")
            result = self.determine_winner(player_choice, computer_choice)
            print(f"Result: {result}\n")

            # Post-game options
            choice = self.handle_post_game_options()
            if choice == "replay":
                self.clear_terminal()
                self.show_instructions()
                continue
            elif choice == "change":
                self.clear_terminal()
                break
            elif choice == "quit":
                self.clear_terminal()
                print("\nThanks for playing! Goodbye!\n")
                exit()

    def show_instructions(self):
        """Displays the game instructions."""
        print("\n****** Welcome to Rock, Paper, Scissors! ******\n")
        print("Choose an option: Rock, Paper, or Scissors.")
        print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.\n")

    def get_player_choice(self):
        """Gets and validates the player's choice."""
        while True:
            try:
                choice = input("Enter your move (Rock, Paper, Scissors): ").capitalize()
                if choice not in self.options:
                    raise ValueError("Invalid choice. Try again.")
                return choice
            except ValueError as e:
                print(e)

    def determine_winner(self, player, computer):
        """
        Determines the result of the game.

        :param player: Player's choice.
        :param computer: Computer's choice.
        :return: Result of the game.
        """
        if player == computer:
            return "It's a draw!"
        elif (player == "Rock" and computer == "Scissors") or \
             (player == "Scissors" and computer == "Paper") or \
             (player == "Paper" and computer == "Rock"):
            return "You win!"
        else:
            return "You lose!"
