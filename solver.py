from typing import Tuple

from board import Board


def solve(board: Board) -> Board:
    progressing: bool = True  # confirm the algorithm is getting closer to a solution and give up if not
    current_board = Board(board.flatten())  # clone the board to safely mutate it
    while progressing and not board.is_solved():
        previous_board = Board(current_board.flatten())

        # todo apply the actual solving rules here

        progressing = previous_board.current_state() != current_board.current_state()

    return current_board
