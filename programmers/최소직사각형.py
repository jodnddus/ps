# https://programmers.co.kr/learn/courses/30/lessons/86491
from test import check_test_case


def solution(sizes):
    big = []
    small = []

    for size in sizes:
        if size[1] > size[0]:
            big.append(size[1])
            small.append(size[0])
        else:
            big.append(size[0])
            small.append(size[1])

    return max(big) * max(small)


check_test_case(solution([[60, 50], [30, 70], [60, 30], [80, 40]]), 4000)
check_test_case(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]), 120)
check_test_case(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]), 133)
