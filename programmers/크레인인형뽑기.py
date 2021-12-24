from test import check_test_case


def exchange_xy(board):
    board_length = len(board)
    new_board = []

    for i in range(board_length):
        new_board.append([])

    for column in board:
        for index in range(len(column)):
            new_board[index].append(column[index])

    return new_board


def solution(board, moves):
    new_board = exchange_xy(board)

    for position in moves:
        print(new_board[position-1])

    answer = 0
    return answer


check_test_case(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
    4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]), 4)
