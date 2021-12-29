# https://programmers.co.kr/learn/courses/30/lessons/70128
from test import check_test_case


def solution(a, b):
    numbers = []
    
    for a_number, b_number in zip(a, b):
        numbers.append(a_number * b_number)

    return sum(numbers)


check_test_case(solution([1, 2, 3, 4], [-3, -1, 0, 2]), 3)
check_test_case(solution([-1, 0, 1], [1, 0, -1]), -2)
