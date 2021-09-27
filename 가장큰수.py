def check_test_case(expect, result):
    if expect == result:
        print("PASS")
    else:
        print("ERR")


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

check_test_case(solution([6, 10, 2]), "6210")
check_test_case(solution([3, 30, 34, 5, 9]), "9534330")
