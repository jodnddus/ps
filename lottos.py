# https://programmers.co.kr/learn/courses/30/lessons/77484

def check_test_case(expect, result):
    if expect == result:
        print("PASS")
    else:
        print("ERR")


def solution(lottos, win_nums):
    same_number_counts = len(set(lottos) & set(win_nums))
    zero_counts = lottos.count(0)
    return [7 - max(same_number_counts+zero_counts, 1), 7 - max(same_number_counts, 1)]


check_test_case(solution([44, 1, 0, 0, 31, 25],
                [31, 10, 45, 1, 6, 19]),	[3, 5])
check_test_case(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]), [1, 6])
check_test_case(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]), [1, 1])
