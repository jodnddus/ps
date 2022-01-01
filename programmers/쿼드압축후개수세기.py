# https://programmers.co.kr/learn/courses/30/lessons/68936
# https://jinomadstory.tistory.com/45
from test import check_test_case
from itertools import chain


def quad(arr):
    arr_len = len(arr)
    unit = arr_len // 2
    arr_sum = sum(chain(*arr))

    if arr_len == 1:
        return [arr[0][0]]
    elif arr_sum == arr_len ** 2:
        return [1]
    elif arr_sum == 0:
        return [0]

    arr1 = [ar[0:unit] for ar in arr[0:unit]]
    arr2 = [ar[unit:] for ar in arr[0:unit]]
    arr3 = [ar[0:unit] for ar in arr[unit:]]
    arr4 = [ar[unit:] for ar in arr[unit:]]

    results = quad(arr1) + quad(arr2) + quad(arr3) + quad(arr4)
    return list(chain(results))


def solution(arr):
    results = quad(arr)
    return [results.count(0), results.count(1)]


check_test_case(solution([[1, 1, 0, 0], [1, 0, 0, 0],
                [1, 0, 0, 1], [1, 1, 1, 1]]), [4, 9])
check_test_case(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [
                0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]), [10, 15])
