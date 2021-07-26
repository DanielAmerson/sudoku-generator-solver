from solver import solve

from board import Board


def test_complete_boards_are_unchanged():
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

    original_board = Board(matrix)
    solved_board = solve(original_board)

    assert original_board.flatten() == solved_board.flatten()
    assert solved_board.is_solved()
    assert solved_board.is_valid()


def test_invalid_boards_are_unchanged():
    matrix = [
        [1, 1, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
    ]

    original_board = Board(matrix)
    solved_board = solve(original_board)

    assert original_board.flatten() == solved_board.flatten()
    assert not solved_board.is_solved()
    assert not solved_board.is_valid()


def test_simple_incomplete_boards_are_solved():
    matrix = [
        [0, 0, 0, 5, 9, 0, 0, 3, 7],
        [0, 7, 9, 0, 3, 2, 0, 8, 0],
        [0, 0, 8, 7, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 1, 6, 2, 0],
        [0, 9, 0, 0, 0, 6, 3, 7, 0],
        [7, 2, 0, 3, 0, 0, 1, 5, 8],
        [0, 0, 0, 0, 0, 7, 8, 6, 5],
        [0, 8, 7, 0, 1, 0, 2, 4, 0],
        [0, 5, 4, 6, 0, 0, 7, 0, 0]
    ]

    solution = [
        [1, 6, 2, 5, 9, 8, 4, 3, 7],
        [4, 7, 9, 1, 3, 2, 5, 8, 6],
        [5, 3, 8, 7, 6, 4, 9, 1, 2],
        [3, 4, 5, 8, 7, 1, 6, 2, 9],
        [8, 9, 1, 2, 5, 6, 3, 7, 4],
        [7, 2, 6, 3, 4, 9, 1, 5, 8],
        [9, 1, 3, 4, 2, 7, 8, 6, 5],
        [6, 8, 7, 9, 1, 5, 2, 4, 3],
        [2, 5, 4, 6, 8, 3, 7, 9, 1]
    ]

    original_board = Board(matrix)
    solved_board = solve(original_board)

    solution_board = Board(solution)

    assert original_board.flatten() != solved_board.flatten()
    assert solved_board.is_solved()
    assert solved_board.is_valid()
    assert solved_board.flatten() == solution_board.flatten()


def test_moderate_incomplete_boards_are_solved():
    matrix = [
        [0, 2, 0, 5, 4, 0, 0, 1, 0],
        [0, 0, 0, 8, 0, 1, 0, 5, 0],
        [5, 0, 0, 6, 7, 0, 0, 0, 4],
        [4, 9, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 7, 4, 5],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 3, 0, 8],
        [1, 0, 0, 0, 6, 3, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0]
    ]

    solution = [
        [8, 2, 7, 5, 4, 9, 6, 1, 3],
        [6, 4, 9, 8, 3, 1, 2, 5, 7],
        [5, 3, 1, 6, 7, 2, 9, 8, 4],
        [4, 9, 6, 1, 5, 7, 8, 3, 2],
        [2, 1, 8, 3, 9, 6, 7, 4, 5],
        [7, 5, 3, 2, 8, 4, 1, 9, 6],
        [9, 6, 2, 4, 1, 5, 3, 7, 8],
        [1, 8, 5, 7, 6, 3, 4, 2, 9],
        [3, 7, 4, 9, 2, 8, 5, 6, 1]
    ]

    original_board = Board(matrix)
    solved_board = solve(original_board)

    solution_board = Board(solution)

    assert original_board.flatten() != solved_board.flatten()
    assert solved_board.is_solved()
    assert solved_board.is_valid()
    assert solved_board.flatten() == solution_board.flatten()


def test_incomplete_boards_with_x_wings_are_solved():
    matrix = [
        [6, 0, 0, 0, 9, 0, 0, 0, 7],
        [0, 4, 0, 0, 0, 7, 1, 0, 0],
        [0, 0, 2, 8, 0, 0, 0, 5, 0],
        [8, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 8],
        [0, 5, 0, 0, 0, 2, 3, 0, 0],
        [0, 0, 4, 5, 0, 0, 0, 2, 0],
        [9, 0, 0, 0, 3, 0, 0, 0, 4],
    ]

    solution = [
        [6, 8, 3, 1, 9, 5, 2, 4, 7],
        [5, 4, 9, 6, 2, 7, 1, 8, 3],
        [7, 1, 2, 8, 4, 3, 9, 5, 6],
        [8, 6, 5, 3, 1, 4, 7, 9, 2],
        [4, 9, 1, 2, 7, 8, 6, 3, 5],
        [2, 3, 7, 9, 5, 6, 4, 1, 8],
        [1, 5, 6, 4, 8, 2, 3, 7, 9],
        [3, 7, 4, 5, 6, 9, 8, 2, 1],
        [9, 2, 8, 7, 3, 1, 5, 6, 4]
    ]

    original_board = Board(matrix)
    solved_board = solve(original_board)

    solution_board = Board(solution)

    assert original_board.flatten() != solved_board.flatten()
    assert solved_board.is_solved()
    assert solved_board.is_valid()
    assert solved_board.flatten() == solution_board.flatten()