# https://programmers.co.kr/learn/courses/30/lessons/12917
from test import check_test_case


def solution(s):
    return ''.join(sorted(list(s), reverse=True))


check_test_case(solution("Zbcdefg"), "gfedcbZ")
