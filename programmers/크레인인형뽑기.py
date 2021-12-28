# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

from test import check_test_case


def pop_doll(board, position):
    depth_length = len(board)

    for depth in range(depth_length):
        picked = board[depth][position]

        if picked != 0:
            board[depth][position] = 0
            return board, picked

    return board, None


def calc_deleted_doll(basket):
    delete_count = 0
    index = 0

    if len(basket) == 0:
        return 0

    while True:
        if len(basket) == 0:
            break

        if index == len(basket) - 1:
            break

        if basket[index] == basket[index + 1]:
            del basket[index + 1], basket[index]
            delete_count += 2
            index = 0
            continue

        index += 1

    return delete_count


def solution(board, moves):
    basket = []

    for position in moves:
        new_board, picked = pop_doll(board, position - 1)

        board = new_board

        if picked != None:
            basket.append(picked)

    answer = calc_deleted_doll(basket)
    return answer


check_test_case(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
    4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]), 4)
check_test_case(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
                0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [1, 5, 3, 5, 1, 2, 1, 4]), 0)
check_test_case(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 3, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 0, 0, 3]], [1, 5, 3, 5, 1, 2, 1, 4]), 2)
