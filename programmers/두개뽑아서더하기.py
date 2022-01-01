# https://programmers.co.kr/learn/courses/30/lessons/68644
from test import check_test_case
from itertools import permutations


def solution(numbers):
    all_case = list(permutations(numbers, 2))
    all_sums = map(lambda nums: nums[0] + nums[1], all_case)
    no_duplicates_sums = set(all_sums)
    
    return sorted(no_duplicates_sums)


check_test_case(solution([2, 1, 3, 4, 1]), [2, 3, 4, 5, 6, 7])
check_test_case(solution([5, 0, 2, 7]), [2, 5, 7, 9, 12])
