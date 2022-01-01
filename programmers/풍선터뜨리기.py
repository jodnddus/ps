# https://programmers.co.kr/learn/courses/30/lessons/68646
# https://velog.io/@eehwan/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%92%8D%EC%84%A0-%ED%84%B0%ED%8A%B8%EB%A6%AC%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
from test import check_test_case


def solution(a):
    answer = [False for _ in range(len(a))]
    left, right = float('inf'), float('inf')

    for i in range(len(a)):
        if a[i] < left:
            answer[i] = True
            left = a[i]
        if a[-1-i] < right:
            answer[-1-i] = True
            right = a[-1-i]

    return sum(answer)


check_test_case(solution([9, -1, -5]), 3)
check_test_case(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]), 6)
