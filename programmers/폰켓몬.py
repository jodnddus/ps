# https://programmers.co.kr/learn/courses/30/lessons/1845

from test import check_test_case

def solution(nums):
    answer = 0

    for num in list(set(nums)):
        if (len(nums) / 2) > answer:
            answer += 1

    return answer

check_test_case(solution([3,1,2,3]), 2)
check_test_case(solution([3,3,3,2,2,4]), 3)
check_test_case(solution([3,3,3,2,2,2]), 2)