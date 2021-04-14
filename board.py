from copy import deepcopy
from typing import List


class Board:
    def __init__(self, input_board: List[List[int]]):  # row => column
        # initialize a default board
        self.__board = [[[] for _ in range(1, 10)] for _ in range(9)]

        # copy and populate
        for column_num in range(9):
            for cell_num in range(9):
                input_value = input_board[column_num][cell_num]
                self.__board[column_num][cell_num] = [input_value] if 1 <= input_value <= 9 else list(range(1, 10))

    def current_state(self):
        return deepcopy(self.__board)
