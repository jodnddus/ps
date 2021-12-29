# https://programmers.co.kr/learn/courses/30/lessons/12977
from test import check_test_case
from itertools import combinations


def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def solution(nums):
    prime_number = []
    numbers = list(combinations(nums, 3))

    for number in numbers:
        if is_prime_num(sum(number)):
            prime_number.append(number)

    return len(prime_number)


check_test_case(solution([1, 2, 3, 4]), 1)
check_test_case(solution([1, 2, 7, 6, 4]), 4)
