# https://programmers.co.kr/learn/courses/30/lessons/42889
from test import check_test_case


def get_failure_rate(stage, stages):
    if len(stages) == 0:
        rate = 0
    else:
        rate = stages.count(stage) / len(stages)

    new_stages = list(filter(lambda x: x != stage, stages))

    return rate, new_stages


def solution(N, stages):
    rates = []

    for stage in range(1, N+1):
        rate, new_stages = get_failure_rate(stage, stages)
        rates.append([stage, rate])
        stages = new_stages

    sorted_rates = sorted(rates, key=lambda stage: stage[1], reverse=True)
    answer = list(map(lambda stage: stage[0], sorted_rates))
    return answer


check_test_case(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]), [3, 4, 2, 1, 5])
check_test_case(solution(4, [4, 4, 4, 4, 4]), [4, 1, 2, 3])
