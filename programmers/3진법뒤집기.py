# https://programmers.co.kr/learn/courses/30/lessons/68935
from test import check_test_case


def n_ary(n, base):
    result = []
    while n > 0:
        n, r = divmod(n, base)
        result.append(r)
    return ''.join(map(str, result))


def solution(n):
    return int(n_ary(n, 3), 3)


check_test_case(solution(45), 7)
check_test_case(solution(125), 229)
