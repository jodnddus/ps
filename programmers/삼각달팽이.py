# https://programmers.co.kr/learn/courses/30/lessons/68645
# https://coding-lks.tistory.com/56
from test import check_test_case


def solution(n):
    piramid = [[0] * n for _ in range(n)]
    x, y = -1, 0
    num = 1
    answer = []

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1

            piramid[x][y] = num
            num += 1

    for i in piramid:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer


check_test_case(solution(4), [1, 2, 9, 3, 10, 8, 4, 5, 6, 7])
check_test_case(solution(5), [1, 2, 12, 3, 13,
                11, 4, 14, 15, 10, 5, 6, 7, 8, 9])
check_test_case(solution(6), [1, 2, 15, 3, 16, 14, 4,
                17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11])
