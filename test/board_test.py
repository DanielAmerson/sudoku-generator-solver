from copy import deepcopy
from pytest import fixture

from board import Board


@fixture
def complete_valid_board():
    matrix = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
    ]

    return Board(matrix)


@fixture
def incomplete_valid_board():
    matrix = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 0, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
    ]

    return Board(matrix)

@fixture
def incomplete_valid_board_rotated():
    matrix = [
        [9, 6, 3, 8, 5, 2, 7, 4, 1],
        [1, 7, 4, 9, 6, 3, 8, 5, 2],
        [2, 8, 5, 1, 7, 4, 9, 6, 3],
        [3, 9, 6, 2, 8, 5, 1, 7, 4],
        [4, 1, 7, 3, 0, 6, 2, 8, 5],
        [5, 2, 8, 4, 1, 7, 3, 9, 6],
        [6, 3, 9, 5, 2, 8, 4, 1, 7],
        [7, 4, 1, 6, 3, 9, 5, 2, 8],
        [8, 5, 2, 7, 4, 1, 6, 3, 9]
    ]

    return Board(matrix)


@fixture
def complete_invalid_board():
    matrix = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 1, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
    ]

    return Board(matrix)


@fixture
def incomplete_invalid_board():
    matrix = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 1, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 0, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
    ]

    return Board(matrix)


def test_complete_and_valid_board_is_valid(complete_valid_board):
    assert complete_valid_board.is_valid()


def test_incomplete_but_valid_board_is_valid(incomplete_valid_board):
    assert incomplete_valid_board.is_valid()


def test_complete_but_invalid_board_is_not_valid(complete_invalid_board):
    assert not complete_invalid_board.is_valid()


def test_incomplete_and_invalid_board_is_not_valid(incomplete_invalid_board):
    assert not incomplete_invalid_board.is_valid()


def test_complete_and_valid_board_is_solved(complete_valid_board):
    assert complete_valid_board.is_solved()


def test_incomplete_but_valid_board_is_not_solved(incomplete_valid_board):
    assert not incomplete_valid_board.is_solved()


def test_complete_but_invalid_board_is_not_solved(complete_invalid_board):
    assert not complete_invalid_board.is_solved()


def test_incomplete_and_invalid_board_is_not_solved(incomplete_invalid_board):
    assert not incomplete_invalid_board.is_solved()


def test_boards_equal_themselves(incomplete_valid_board):
    assert incomplete_valid_board == incomplete_valid_board


def test_different_boards_with_same_state_are_equal(incomplete_valid_board):
    cloned_board = deepcopy(incomplete_valid_board)

    assert cloned_board is not incomplete_valid_board
    assert cloned_board == incomplete_valid_board


def test_different_board_states_are_not_equal(incomplete_valid_board, complete_valid_board):
    assert incomplete_valid_board != complete_valid_board


def test_rotation(incomplete_valid_board, incomplete_valid_board_rotated):
    incomplete_valid_board.rotate()

    assert incomplete_valid_board == incomplete_valid_board_rotated
