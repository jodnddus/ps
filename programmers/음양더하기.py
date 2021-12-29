# https://programmers.co.kr/learn/courses/30/lessons/76501
from test import check_test_case


def solution(absolutes, signs):
    numbers = []

    for index in range(len(absolutes)):
        if signs[index]:
            numbers.append(absolutes[index])
        else:
            numbers.append(absolutes[index] * -1)

    return sum(numbers)


check_test_case(solution([4, 7, 12], [True, False, True]), 9)
check_test_case(solution([1, 2, 3], [False, False, True]), 0)
