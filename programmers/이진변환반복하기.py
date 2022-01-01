# https://programmers.co.kr/learn/courses/30/lessons/70129
from test import check_test_case
from re import sub


def transform(s): return s.count('0'), bin(len(sub("0", "", s)))[2:]


def solution(s):
    answer = [0, 0]

    while True:
        if s == '1':
            break

        zero_count, new_s = transform(s)
        s = new_s

        answer[0] += 1
        answer[1] += zero_count

    return answer


check_test_case(solution("110010101001"), [3, 8])
check_test_case(solution("01110"), [3, 3])
check_test_case(solution("1111111"), [4, 1])
