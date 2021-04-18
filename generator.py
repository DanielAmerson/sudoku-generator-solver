from random import shuffle
from typing import List, Set, Tuple

from board import Board


def generate_game() -> Board:  # todo accept parameter indicating special game types (cages, thermo, etc.)
    board = Board([[0 for _ in range(9)] for _ in range(9)])

    # start by generating a valid/completed board
    all_cell_options = set(range(1, 10))  # this should probably be an immutable field on Board
    for row_number in range(9):
        column_options: List[Tuple[int, Set[int]]] = []

        # find the remaining options for each cell in the row
        for col_number in range(9):
            remaining_cell_options: Set[int] = all_cell_options - board.values_seen_by_cell(row_number, col_number)
            column_options.append((col_number, remaining_cell_options))

        # loop through each option and pick/assign an option from the most restricted column until all cells are filled
        while len(column_options) > 0:
            # re-sort on each iteration as the usage of an option might change the most restricted ordering
            column_options.sort(key=lambda element: len(element[1]))
            most_restricted_cell: Tuple[int, Set[int]] = column_options.pop(0)

            cell_options: List[int] = list(most_restricted_cell[1])
            shuffle(cell_options)
            cell_value = cell_options[0]
            board.assign_value(row_number, most_restricted_cell[0], cell_value)

            # remove the selected option from the remaining elements so it won't be reselected
            for column_option in column_options:
                if cell_value in column_option[1]:
                    column_option[1].remove(cell_value)

    # todo randomly remove values and determine if the solver can solve it
    # if it can, remove more values and try to solve again
    # once the board can no longer be solved by the algorithm in this project, return the most recently solvable board

    return board


