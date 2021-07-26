from copy import deepcopy
from typing import Dict, List, FrozenSet, Set, Tuple

from board import Board


def solve(board: Board) -> Board:
    progressing: bool = True  # confirm the algorithm is getting closer to a solution and give up if not
    current_board = deepcopy(board)  # clone the board to safely mutate it
    if current_board.is_valid():
        while progressing and not current_board.is_solved():
            previous_board = deepcopy(current_board)

            # apply basic Sudoku rules by filtering on n-tuples
            filter_restricted_tuples(current_board)

            # todo when allowing difficulty to be applied, don't use this rule for easy boards
            filter_x_wing_values(current_board)

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


# todo this logic is currently looking only at column X-Wings (add logic to rotate the board)
def filter_x_wing_values(board: Board):
    for value in range(1, 10):
        potential_x_wing_coords: [Set[int]] = [set() for _ in range(9)]  # column: [rows]
        for column in range(9):
            rows_with_value: Set[int] = set()
            for row in range(9):
                if value in board.options_at_location(row, column):
                    rows_with_value.add(row)
            if len(rows_with_value) == 2:  # 3 for swordfish?
                potential_x_wing_coords[column] = rows_with_value

        rows_to_column_map: {Tuple[int, int]: Set[int]} = {}
        for column in range(9):
            rows = tuple(potential_x_wing_coords[column])
            if rows:
                if rows not in rows_to_column_map:
                    rows_to_column_map[rows] = set()
                rows_to_column_map[rows].add(column)

        for rows in rows_to_column_map:
            columns = rows_to_column_map[rows]
            if len(columns) == 2:  # 3 for swordfish?
                columns_to_remove_entry = [column for column in range(9) if column not in columns]
                for row in rows:
                    for column in columns_to_remove_entry:
                        current_options: Set[int] = set(board.options_at_location(row, column))
                        remaining_options: Set[int] = current_options - {value}
                        board.assign_value(row, column, remaining_options)


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
