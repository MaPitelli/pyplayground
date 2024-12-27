from games.rock_paper_scissors import RockPaperScissors
from games.hangman import Hangman
from games.tic_tac_toe import TicTacToe
from games.minesweeper import Minesweeper


def main():
    games = {
        1: RockPaperScissors(),
        2: Hangman(),
        3: TicTacToe(),
        4: Minesweeper()
    }

    while True:
        print("""
            Choose a game to play:

                1. Rock, Paper, Scissors
                2. Hangman
                3. Tic-Tac-Toe
                4. Minesweeper
                5. Exit
            
            """)

        try:
            choice = int(input("Enter the number of the game you want to play: "))
            if choice in games:
                games[choice].show_instructions()
                games[choice].play()
            elif choice == 5:
                print("\nThanks for playing! Goodbye!\n")
                break
            else:
                print("\nInvalid choice. Please choose a valid option.")
        except ValueError:
            print("\nPlease enter a number.")

if __name__ == "__main__":
    main()

