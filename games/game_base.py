from abc import ABC, abstractmethod

class GameBase(ABC):
    """Abstract base class for all games. Defines the basic structure of a game."""

    def __init__(self, name):
        """
        Initializes a new game.
        
        :param name: The name of the game.
        """
        self.name = name

    @abstractmethod
    def show_instructions(self):
        """Displays instructions for the game."""
        pass

    @abstractmethod
    def play(self):
        """Runs the main game loop."""
        pass

    def handle_post_game_options(self):
        """
        Handles options after the game ends: replay, quit, or change game.

        :return: A string representing the player's choice ('replay', 'change', or 'quit').
        """
        while True:
            print("\nWhat would you like to do next?")
            print("1. Play the same game again")
            print("2. Choose another game")
            print("3. Exit the program")
            choice = input("Enter your choice (1, 2, or 3): ").strip()

            if choice == "1":
                return "replay"
            elif choice == "2":
                return "change"
            elif choice == "3":
                return "quit"
            else:
                print("\nInvalid choice. Please try again.")
