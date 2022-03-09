from test import check_test_case


def solution(citations):
    citations_len = len(citations)
    result = 0

    for i in reversed(range(1, citations_len+1)):
        if len(list(filter(lambda citation: citation >= i, citations))) >= i:
            return i

    return result


check_test_case(solution([3, 0, 6, 1, 5]), 3)
check_test_case(solution([0, 0, 0, 0, 0]), 0)
check_test_case(solution([5, 4, 3, 2, 1]), 3)
check_test_case(solution([5, 4, 2, 2, 1]), 2)
