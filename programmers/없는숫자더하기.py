# https://programmers.co.kr/learn/courses/30/lessons/86051
from test import check_test_case


def solution(numbers):
    return 45 - sum(numbers)


check_test_case(solution([1, 2, 3, 4, 6, 7, 8, 0]), 14)
check_test_case(solution([5, 8, 4, 0, 6, 7, 9]), 6)
