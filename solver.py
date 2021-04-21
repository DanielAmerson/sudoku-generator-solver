from copy import deepcopy

from board import Board


def solve(board: Board) -> Board:
    progressing: bool = True  # confirm the algorithm is getting closer to a solution and give up if not
    current_board = Board(board.flatten())  # clone the board to safely mutate it
    if current_board.is_valid():
        while progressing and not board.is_solved():
            previous_board = deepcopy(current_board)

            for row in range(9):
                for column in range(9):
                    if len(current_board.options_at_location(row, column)) > 1:  # confirm the cell isn't already solved
                        # gather up all the currently solved values
                        values_seen_by_cell = set(current_board.values_seen_by_cell(row, column))
                        # the only options are what's left out of the normal 1-9 (basic Sudoku rules here)
                        remaining_possibilities = set(range(1, 10)) - values_seen_by_cell
                        current_board.assign_value(row, column, list(remaining_possibilities))

            # todo apply more advanced techniques
            progressing = previous_board.current_state() != current_board.current_state()

    return current_board
