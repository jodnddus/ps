# https://programmers.co.kr/learn/courses/30/lessons/81302
from test import check_test_case
from itertools import combinations


def listed(place):
    new_place = []
    p_info = []

    for row_index, row in enumerate(place):
        listed_row = list(row)

        for item_index, item in enumerate(listed_row):
            if item == 'P':
                p_info.append([row_index, item_index])

        new_place.append(listed_row)

    return new_place, p_info


def get_manhattan_distance(node1, node2):
    x_node1, y_node1 = node1
    x_node2, y_node2 = node2

    return abs(x_node1 - x_node2) + abs((y_node1 - y_node2))


def check_keep_distance(place, p_info):
    print(list(filter(lambda nodes: get_manhattan_distance(
        nodes[0], nodes[1]) <= 2, list(combinations(p_info, 2)))))


def solution(places):
    answer = []

    for place in places:
        place, p_info = listed(place)
        answer.append(check_keep_distance(place, p_info))

    return answer


check_test_case(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], [
                "PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]), [1, 0, 1, 1, 1])
