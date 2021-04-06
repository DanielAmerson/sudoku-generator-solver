from enum import Enum


class Mode(Enum):
    GENERATE = 1
    SOLVE = 2


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
        print("In the future you might be able to actually input incomplete board data here...")
