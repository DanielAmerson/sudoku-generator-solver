from enum import Enum

from board import Board


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
        print("Doing some very computationally expensive work to generate a board for you...")
    else:
        print("Enter each line of the Sudoku board with no spaces.  Mark unknown digits with 0.")
        print("Example: 123056780")
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
