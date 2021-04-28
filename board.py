from copy import deepcopy
from typing import List, Set


class Board:
    def __init__(self, input_board: List[List[int]]):  # row => column
        # initialize a default board
        self.__board = [[set() for _ in range(9)] for _ in range(9)]

        # copy and populate
        for column_num in range(9):
            for cell_num in range(9):
                input_value = input_board[column_num][cell_num]
                self.__board[column_num][cell_num] = {input_value} if 1 <= input_value <= 9 else set(range(1, 10))

    def current_state(self) -> List[List[Set[int]]]:
        return deepcopy(self.__board)

    def flatten(self) -> List[List[int]]:  # todo cache this result and only regenerate when the board changes
        result: List[List[int]] = [[0 for _ in range(1, 10)] for _ in range(9)]
        for column_num in range(9):
            for cell_num in range(9):
                board_value = self.__board[column_num][cell_num]
                result[column_num][cell_num] = list(board_value)[0] if len(board_value) == 1 else 0

        return result

    def assign_value(self, row_num: int, column_num: int, values: Set[int]):
        values_to_assign = deepcopy(values) if all(1 <= value <= 9 for value in values) else set(range(1, 10))
        self.__board[row_num][column_num] = values_to_assign

    def options_at_location(self, row_num, col_num) -> Set[int]:
        return self.__board[row_num][col_num]

    def solved_values_in_row(self, row_num) -> List[int]:
        return Board.__values_in_cells(self.__board[row_num])

    def solved_values_in_column(self, col_num) -> List[int]:
        return Board.__values_in_cells([element[col_num] for element in self.__board])

    def solved_values_in_box_at_location(self, row_num, col_num) -> List[int]:
        box_row_start = (row_num // 3) * 3
        box_col_start = (col_num // 3) * 3

        cells: List[Set[int]] = []
        for row_value in range(box_row_start, box_row_start + 3):
            for col_value in range(box_col_start, box_col_start + 3):
                cells.append(self.__board[row_value][col_value])

        return Board.__values_in_cells(cells)

    def values_seen_by_cell(self, row_num, column_num) -> Set[int]:
        return set(self.solved_values_in_row(row_num) + self.solved_values_in_column(column_num) +
                   self.solved_values_in_box_at_location(row_num, column_num))

    def is_solved(self):
        complete_value_set = set(range(1, 10))
        for row in range(9):
            for col in range(9):
                # todo clean up duplicated code in is_valid
                row_values = self.solved_values_in_row(row)
                column_values = self.solved_values_in_column(col)
                box_values = self.solved_values_in_box_at_location(row, col)
                if not Board.__cell_is_valid(row_values, column_values, box_values):
                    return False

                if complete_value_set != set(row_values) or \
                        complete_value_set != set(column_values) or \
                        complete_value_set != set(box_values):
                    return False

        return True

    def is_valid(self):
        for row in range(9):
            for col in range(9):
                row_values = self.solved_values_in_row(row)
                column_values = self.solved_values_in_column(col)
                box_values = self.solved_values_in_box_at_location(row, col)
                if not Board.__cell_is_valid(row_values, column_values, box_values):
                    return False

        return True

    def pretty_print(self, show_pencil_marks=False):
        row_divider = ' --- ' * 9
        for row in range(9):
            print(row_divider)
            cell_row1 = ''
            cell_row2 = ''
            cell_row3 = ''
            for column in range(9):
                possibilities = set(self.__board[row][column])
                if len(possibilities) == 1:
                    cell_row1 = cell_row1 + Board.__fill_cell()
                    cell_row2 = cell_row2 + Board.__fill_cell(cell2=possibilities.pop())
                    cell_row3 = cell_row3 + Board.__fill_cell()
                elif not show_pencil_marks:
                    cell_row1 = cell_row1 + Board.__fill_cell()
                    cell_row2 = cell_row2 + Board.__fill_cell()
                    cell_row3 = cell_row3 + Board.__fill_cell()
                else:
                    cell_row1 = cell_row1 + Board.__determine_marks_for_row(0, possibilities)
                    cell_row2 = cell_row2 + Board.__determine_marks_for_row(1, possibilities)
                    cell_row3 = cell_row3 + Board.__determine_marks_for_row(2, possibilities)
            print(cell_row1)
            print(cell_row2)
            print(cell_row3)

        print(row_divider)

    @staticmethod
    def __determine_marks_for_row(row_num: int, possibilities: Set[int]):
        row_values = range((row_num * 3) + 1, (row_num * 3) + 4)
        return Board.__fill_cell(
            cell1=row_values[0] if row_values[0] in possibilities else ' ',
            cell2=row_values[1] if row_values[1] in possibilities else ' ',
            cell3=row_values[2] if row_values[2] in possibilities else ' '
        )

    @staticmethod
    def __fill_cell(cell1=' ', cell2=' ', cell3=' '):
        return '|{0}{1}{2}|'.format(cell1, cell2, cell3)

    @staticmethod
    def __cell_is_valid(row_values, column_values, box_values):
        if len(row_values) != len(set(row_values)) or \
                len(column_values) != len(set(column_values)) or \
                len(box_values) != len(set(box_values)):
            return False
        all_values = row_values + column_values + box_values
        all_values.sort()
        if all_values[0] < 1 or all_values[-1] > 9:  # this shouldn't be possible with the current interface
            return False
        return True

    @staticmethod
    def __values_in_cells(cells: List[Set[int]]) -> List[int]:
        return [list(element)[0] for element in cells if len(element) == 1]
