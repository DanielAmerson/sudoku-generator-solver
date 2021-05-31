from enum import Enum
from random import seed
from sys import argv
from time import time

from board import Board
from generator import generate_game
from solver import solve


class Mode(Enum):
    GENERATE = 1
    SOLVE = 2


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    seed_value = int(time())
    if len(argv) > 1:
        try:
            seed_value = int(argv[1])
        except ValueError:
            print("Provided seed value was ignored as it was not an integer.")

    seed(seed_value)
    print("Seed set to {0}.  To reproduce this run, provide this value during start up.".format(seed_value))

    mode = None
    while True:
        option = input("Enter (1) to generate a Sudoku board or (2) to solve an existing board: ")
        if option == "1":
            mode = Mode.GENERATE
            break
        elif option == "2":
            mode = Mode.SOLVE
            break
        else:
            print("Input invalid.")

    if mode == Mode.GENERATE:
        game_board = generate_game()
        print("Board has been generated:")
        game_board.pretty_print()
    else:
        print("Enter each line of the Sudoku board with no spaces.  Mark unknown digits with 0.")
        print("Example: 123056780 when column 4 and 9 require values")
        entered_board = []
        while len(entered_board) < 9:
            line = input("Enter line {0}: ".format(len(entered_board) + 1))
            if len(line) != 9:
                print("Input should be 9 numbers long.")
            elif not is_integer(line):
                print("Only numbers should be entered")
            else:
                entered_board.append([int(char) for char in line])

        board_to_solve = Board(entered_board)
        result = solve(board_to_solve)

        if result.is_solved():
            print("A unique solution to the puzzle was found.")
            result.pretty_print()
        else:
            print("A unique solution to the puzzle could not be found.")
            result.pretty_print(True)
