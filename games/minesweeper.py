import random
from games.game_base import GameBase

class Minesweeper(GameBase):
    """Class for the Minesweeper game."""

    def __init__(self):
        """Initializes the game with the name 'Minesweeper'."""
        super().__init__("Minesweeper")
        self.board_size = 5  # 5x5 board
        self.num_mines = 5  # Number of mines
        self.reset_game()

    def reset_game(self):
        """Resets the game to its initial state."""
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.revealed = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.mines = self.place_mines()
        self.game_over = False

    def show_instructions(self):
        """Displays the game instructions."""
        print("\n****** Welcome to Minesweeper! ******\n")
        print("You need to reveal all the spaces without triggering a mine.")
        print("You can reveal a square by entering the row and column numbers (e.g., 1 2 for row 1, column 2).")
        print("If you trigger a mine, the game is over!")

    def play(self):
        """Executes the main game logic."""
        while not self.game_over:
            self.display_board()
            row, col = self.get_player_move()

            # Check if the player hit a mine
            if self.board[row][col] == 'X':
                self.display_board(reveal_all=True)  # Mostrar todas las minas
                print("\nBoom! You hit a mine! Game over.")
                self.game_over = True
            else:
                self.reveal_square(row, col)

                if self.check_win():
                    self.display_board(reveal_all=True)  # Mostrar todas las minas
                    print("\nCongratulations! You've cleared the board without hitting any mines!")
                    self.game_over = True

        # Post-game options
        choice = self.handle_post_game_options()
        if choice == "replay":
            self.reset_game() # Reset the game for replay
            self.play()
        elif choice == "change":
            self.reset_game() # Reset the game for replay
            return
        elif choice == "quit":
            print("\nThanks for playing! Goodbye!\n")
            exit()

    def place_mines(self):
        """Randomly places mines on the board."""
        mines = set()
        while len(mines) < self.num_mines:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            if (row, col) not in mines:
                mines.add((row, col))
                self.board[row][col] = 'X'  # Place the mine on the board
        return mines

    def display_board(self, reveal_all=False):
        """
        Displays the current state of the board.

        :param reveal_all: If True, reveals all mines and the player's progress.
        """
        print("\nCurrent board:")
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                if reveal_all:
                    # Show mines and revealed cells
                    row.append(self.board[i][j] if self.board[i][j] == 'X' else self.revealed[i][j])
                else:
                    # Show only revealed cells, hide unrevealed cells with '■'
                    row.append(self.revealed[i][j] if self.revealed[i][j] != ' ' else '■')
            print(" ".join(row))

    def get_player_move(self):
        """
        Gets and validates the player's move.

        :return: A tuple (row, col) of the valid move.
        """
        while True:
            try:
                move = input("Enter your move (row and column, separated by a space): ")
                row, col = map(int, move.split())
                if not (1 <= row <= self.board_size and 1 <= col <= self.board_size):
                    raise ValueError(f"Row and column must be between 1 and {self.board_size}.")
                row, col = row - 1, col - 1  # Convert to 0-based index
                return row, col
            except ValueError as e:
                print(e)

    def reveal_square(self, row, col):
        """Reveals a square and adjacent empty spaces if applicable."""
        # If the square is empty, count surrounding mines
        if self.revealed[row][col] != ' ':
            return

        # Count adjacent mines
        adjacent_mines = self.count_adjacent_mines(row, col)

        # If no adjacent mines, reveal adjacent squares as well
        if adjacent_mines == 0:
            self.revealed[row][col] = '0'
            for i in range(max(0, row - 1), min(self.board_size, row + 2)):
                for j in range(max(0, col - 1), min(self.board_size, col + 2)):
                    if self.revealed[i][j] == ' ' and (i, j) != (row, col):
                        self.reveal_square(i, j)
        else:
            self.revealed[row][col] = str(adjacent_mines)

    def count_adjacent_mines(self, row, col):
        """Counts the number of mines adjacent to a given square."""
        adjacent_mines = 0
        for i in range(max(0, row - 1), min(self.board_size, row + 2)):
            for j in range(max(0, col - 1), min(self.board_size, col + 2)):
                if (i, j) in self.mines:
                    adjacent_mines += 1
        return adjacent_mines

    def check_win(self):
        """Checks if the player has won (all non-mine squares are revealed)."""
        for row in range(self.board_size):
            for col in range(self.board_size):
                if (row, col) not in self.mines and self.revealed[row][col] == ' ':
                    return False
        return True
