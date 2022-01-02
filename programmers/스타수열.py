# https://programmers.co.kr/learn/courses/30/lessons/70130
# https://yabmoons.tistory.com/610

from test import check_test_case
from collections import Counter

def solution(a):
    answer, c = 0, Counter(a)

    if len(a) == 0: return 0

    for k, v in c.items():
        if c[k] * 2 < answer: continue

        star_sequence_length, pointer = 0, 0

        while pointer < len(a) - 1:
            if (a[pointer] != k and a[pointer+1] != k) or a[pointer] == a[pointer+1]:
                pointer += 1
                continue

            star_sequence_length += 2
            pointer += 2

        answer = max(star_sequence_length, answer)

    return answer


check_test_case(solution([0]), 0)
check_test_case(solution([5, 2, 3, 3, 5, 3]), 4)
check_test_case(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]), 8)
check_test_case(
    solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0, 0, 0, 0, 0, 8, 0, 1]), 12)
