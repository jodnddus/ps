from test import check_test_case


def solution(s):
    answer = len(s)

    for step in range(1, len(s)//2+1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j: j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j: j+step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer


check_test_case(solution("aabbaccc"), 7)
check_test_case(solution("ababcdcdababcdcd"), 9)
check_test_case(solution("abcabcdede"), 8)
check_test_case(solution("abcabcabcabcdededededede"), 14)
check_test_case(solution("xababcdcdababcdcd"), 17)
