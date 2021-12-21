from itertools import permutations 

def check_test_case(expect, result):
    if expect == result:
        print("PASS")
    else:
        print("ERR")

def is_exist_head_keyword(keywords):
    if keywords[0].startswith(keywords[1]) or keywords[1].startswith(keywords[0]):
        return False
    return True

def solution(phone_book):
    answer = True

    for keywords in list(permutations(phone_book, 2)):
        if (len(keywords[0]) <= len(keywords[1])):
            answer = is_exist_head_keyword(keywords)
            if not(answer):
                break

    return answer

check_test_case(solution(["119", "97674223", "1195524421"]), False)
check_test_case(solution(["123", "456", "789"]), True)
check_test_case(solution(["12", "123", "1235", "567", "88"]), False)
