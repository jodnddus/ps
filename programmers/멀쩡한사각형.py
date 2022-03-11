from test import check_test_case

import math


def solution(w, h):
    return (w * h) - (w + h - math.gcd(w, h))


check_test_case(solution(8, 12), 80)
