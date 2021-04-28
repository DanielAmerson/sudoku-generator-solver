from copy import deepcopy
from typing import List, Set, Tuple

from board import Board


def solve(board: Board) -> Board:
    progressing: bool = True  # confirm the algorithm is getting closer to a solution and give up if not
    current_board = deepcopy(board)  # clone the board to safely mutate it
    if current_board.is_valid():
        while progressing and not current_board.is_solved():
            previous_board = deepcopy(current_board)

            # apply basic Sudoku rules by filtering on n-tuples
            filter_restricted_tuples(current_board)

            # todo apply more advanced techniques
            progressing = previous_board.current_state() != current_board.current_state()

    return current_board


def filter_restricted_tuples(board: Board):
    for division_count in range(9):  # box x, column x, row x
        box_row_start = (division_count // 3) * 3
        box_column_start = (division_count % 3) * 3

        coords_in_box: Set[Tuple[int, int]] = {
            (row + box_row_start, column + box_column_start) for row in range(3) for column in range(3)
        }

        __filter_restricted_tuples_in_coords(board, coords_in_box)  # box...duh
        __filter_restricted_tuples_in_coords(board, {(division_count, entry) for entry in range(9)})  # row
        __filter_restricted_tuples_in_coords(board, {(entry, division_count) for entry in range(9)})  # column


def __filter_restricted_tuples_in_coords(board: Board, coords: Set[Tuple[int, int]], combination: List[int] = None):
    # todo while this appears to be a general purpose solver it is highly inefficient.  likely we need to cache the
    # solved location and skip over the associated values while in this loop
    loop_start = (combination[-1] + 1) if combination else 1
    for entry_to_append in range(loop_start, 10):
        new_combination = (combination + [entry_to_append]) if combination else [entry_to_append]
        if not __filter_restricted_tuples_by_combination_in_coords(board, set(new_combination), coords):
            # if no filtering on this tuple occurred try a recurse and see if a longer combination succeeds
            __filter_restricted_tuples_in_coords(board, coords, new_combination)


def __filter_restricted_tuples_by_combination_in_coords(
    board: Board,
    combination: Set[int],
    coords: Set[Tuple[int, int]]
) -> bool:
    coords_without_extra_options: Set[Tuple[int, int]] = set()
    for entry in coords:
        if len(board.options_at_location(entry[0], entry[1]) - combination) == 0:  # all options are part of combo
            coords_without_extra_options.add(entry)

    if len(combination) == len(coords_without_extra_options):  # pair can only live in 2 places, triple in 3, etc.
        coords_to_restrict = coords - coords_without_extra_options
        for entry_to_restrict in coords_to_restrict:
            current_options: Set[int] = set(board.options_at_location(entry_to_restrict[0], entry_to_restrict[1]))
            remaining_options: Set[int] = current_options - combination
            board.assign_value(entry_to_restrict[0], entry_to_restrict[1], remaining_options)
        return True
    return False
