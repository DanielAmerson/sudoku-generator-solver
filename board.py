from copy import deepcopy
from typing import List, Set


class Board:
    def __init__(self, input_board: List[List[int]]):  # row => column
        # initialize a default board
        self.__board = [[[] for _ in range(9)] for _ in range(9)]

        # copy and populate
        for column_num in range(9):
            for cell_num in range(9):
                input_value = input_board[column_num][cell_num]
                self.__board[column_num][cell_num] = [input_value] if 1 <= input_value <= 9 else list(range(1, 10))

    def current_state(self) -> List[List[List[int]]]:
        return deepcopy(self.__board)

    def flatten(self) -> List[List[int]]:
        result: List[List[int]] = [[0 for _ in range(1, 10)] for _ in range(9)]
        for column_num in range(9):
            for cell_num in range(9):
                board_value = self.__board[column_num][cell_num]
                result[column_num][cell_num] = board_value[0] if len(board_value) == 1 else 0

        return result

    def assign_value(self, row_num, column_num, value):
        self.__board[row_num][column_num] = [value]

    def values_seen_by_cell(self, row_num, column_num) -> Set[int]:
        # todo implement this logic
        return set()

    def is_solved(self):
        # todo implement this logic
        return False
