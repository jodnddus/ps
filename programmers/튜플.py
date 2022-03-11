from test import check_test_case


def solution(s):
    answer = []
    s = sorted(s[2:-2].split('},{'), key=lambda i: len(i))

    for i in s:
        nums = i.split(',')
        for num in nums:
            if num not in answer:
                answer.append(num)

    return list(map(lambda num: int(num), answer))


check_test_case(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"), [2, 1, 3, 4])
check_test_case(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"), [2, 1, 3, 4])
check_test_case(solution("{{20,111},{111}}"), [111, 20])
check_test_case(solution("{{123}}"), [123])
check_test_case(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"), [3, 2, 4, 1])
