from random import shuffle

from board import Board


def generate_game() -> Board:  # todo accept parameter indicating special game types (cages, thermo, etc.)
    board = Board([[0 for _ in range(9)] for _ in range(9)])

    # start by generating a valid/completed board
    for row_number in range(9):
        remaining_row_options = set(range(1, 10))
        for col_number in range(9):
            remaining_cell_options = list(remaining_row_options - board.values_seen_by_cell(row_number, col_number))
            shuffle(remaining_cell_options)

            cell_value = remaining_cell_options[0]
            remaining_cell_options.remove(cell_value)
            board.assign_value(row_number, col_number, cell_value)

    # todo randomly remove values and determine if the solver can solve it
    # if it can, remove more values and try to solve again
    # once the board can no longer be solved by the algorithm in this project, return the most recently solvable board

    return board


