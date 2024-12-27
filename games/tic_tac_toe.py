from games.game_base import GameBase
import random

class TicTacToe(GameBase):
    """Class for the Tic-Tac-Toe game."""

    def __init__(self):
        """Initializes the game with the name 'Tic-Tac-Toe'."""
        super().__init__("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 board

    def show_instructions(self):
        """Displays the game instructions."""
        print("\n****** Welcome to Tic-Tac-Toe! ******\n")
        print("Players take turns to place their mark (X or O) on the board.")
        print("The first player to form a line of three wins!")
        print("To place a mark, enter the row and column numbers (e.g., 1 2 for row 1, column 2).")

    def play(self):
        """Executes the main game logic."""
        while True:  # Loop to allow replaying or changing games
            self.board = [[" " for _ in range(3)] for _ in range(3)]  # Reset board
            mode = input("\nChoose mode: 1 for Player vs Player, 2 for Player vs Computer: ").strip()
            if mode not in {"1", "2"}:
                print("Invalid mode. Please choose 1 or 2.")
                continue

            player_vs_computer = (mode == "2")
            current_player = "X"
            move_count = 0

            while move_count < 9:
                self.display_board()
                print(f"\nPlayer {current_player}'s turn.")

                if player_vs_computer and current_player == "O":
                    row, col = self.computer_move()
                    print(f"Computer chooses: {row + 1} {col + 1}")
                else:
                    row, col = self.get_player_move()

                # Place the mark and update the board
                self.board[row][col] = current_player
                move_count += 1

                # Check for a win
                if self.check_winner(current_player):
                    self.display_board()
                    print(f"\nPlayer {current_player} wins! Congratulations!")
                    break

                # Switch player
                current_player = "O" if current_player == "X" else "X"
            else:
                # If no winner after 9 moves, it's a draw
                self.display_board()
                print("\nIt's a draw! Well played both players.")

            # Post-game options
            choice = self.handle_post_game_options()
            if choice == "replay":
                continue
            elif choice == "change":
                break
            elif choice == "quit":
                print("\nThanks for playing! Goodbye!\n")
                exit()

    def display_board(self):
        """Displays the current state of the board with improved visuals."""
        print("\nCurrent board:\n")
        for i, row in enumerate(self.board):
            print(" | ".join(row))
            if i < 2:  # Add horizontal separators between rows
                print("-" * 9)

    def get_player_move(self):
        """
        Gets and validates the player's move.

        :return: A tuple (row, col) of the valid move.
        """
        while True:
            try:
                move = input("Enter your move (row and column, separated by a space): ")
                row, col = map(int, move.split())
                if not (1 <= row <= 3 and 1 <= col <= 3):
                    raise ValueError("Row and column must be between 1 and 3.")
                row, col = row - 1, col - 1  # Convert to 0-based index
                if self.board[row][col] != " ":
                    raise ValueError("This position is already occupied. Choose another.")
                return row, col
            except ValueError as e:
                print(e)

    def computer_move(self):
        """
        Determines the computer's move with priority to win or block the player.

        :return: A tuple (row, col) of the computer's move.
        """
        # Priority 1: Check if the computer can win in the next move
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    if self.check_winner("O"):
                        self.board[i][j] = " "  # Reset to original state
                        return i, j
                    self.board[i][j] = " "  # Reset to original state

        # Priority 2: Block the player's winning move
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "X"
                    if self.check_winner("X"):
                        self.board[i][j] = " "  # Reset to original state
                        return i, j
                    self.board[i][j] = " "  # Reset to original state

        # Priority 3: Choose a random empty spot
        empty_positions = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        return random.choice(empty_positions)

    def check_winner(self, player):
        """
        Checks if the given player has won.

        :param player: The current player ('X' or 'O').
        :return: True if the player has won, False otherwise.
        """
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Row
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Column
                return True
        if all(self.board[i][i] == player for i in range(3)):  # Diagonal \
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):  # Diagonal /
            return True
        return False





