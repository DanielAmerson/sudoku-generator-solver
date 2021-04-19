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

    def flatten(self) -> List[List[int]]:  # todo cache this result and only regenerate when the board changes
        result: List[List[int]] = [[0 for _ in range(1, 10)] for _ in range(9)]
        for column_num in range(9):
            for cell_num in range(9):
                board_value = self.__board[column_num][cell_num]
                result[column_num][cell_num] = board_value[0] if len(board_value) == 1 else 0

        return result

    def assign_value(self, row_num, column_num, value):
        self.__board[row_num][column_num] = [value] if 1 <= value <= 9 else list(range(1, 10))

    def values_in_row(self, row_num) -> Set[int]:
        return Board.__values_in_cells(self.__board[row_num])

    def values_in_column(self, col_num) -> Set[int]:
        return Board.__values_in_cells([element[col_num] for element in self.__board])

    def values_in_box_at_location(self, row_num, col_num) -> Set[int]:
        box_row_start = (row_num // 3) * 3
        box_col_start = (col_num // 3) * 3

        cells: List[List[int]] = []
        for row_value in range(box_row_start, box_row_start + 3):
            for col_value in range(box_col_start, box_col_start + 3):
                cells.append(self.__board[row_value][col_value])

        return Board.__values_in_cells(cells)

    def values_seen_by_cell(self, row_num, column_num) -> Set[int]:
        if len(self.__board[row_num][column_num]) == 1:
            # if the cell is solved just assume it can 'see' every other value somewhere
            return set(range(1, 10)) - {self.__board[row_num][column_num]}

        return self.values_in_row(row_num) | self.values_in_column(column_num) | \
            self.values_in_box_at_location(row_num, column_num)

    def is_solved(self):
        # todo implement this logic
        return False

    @staticmethod
    def __values_in_cells(cells: List[List[int]]) -> Set[int]:
        return set(element[0] for element in cells if len(element) == 1)
