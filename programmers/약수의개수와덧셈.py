# https://programmers.co.kr/learn/courses/30/lessons/77884
from test import check_test_case


def is_divisor_count_even_odd(num):
    count = 0

    for divisor in range(1, num+1):
        if num % divisor == 0:
            count += 1

    return count % 2


def solution(left, right):
    nums = []

    for num in range(left, right+1):
        if is_divisor_count_even_odd(num):
            nums.append(-1 * num)
        else:
            nums.append(num)

    return sum(nums)


check_test_case(solution(13, 17), 43)
check_test_case(solution(24, 27), 52)
