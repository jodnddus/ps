import re

def check_test_case(expect, result):
    if expect == result:
        print("PASS")
    else:
        print("ERR")

def check_id_length(id):
    id_length = len(id)
    if id_length >= 3 and id_length <= 15:
        return True
    return False

def check_available_word(id):
    available_word_checker = re.compile('^[0-9a-z\-\_\.]*$')
    result = available_word_checker.match(id)
    if result:
        return True
    return False

def check_dot_rule(id):
    available_word_checker = re.compile('\.{2,}')
    result = available_word_checker.match(id)
    if result:
        return False 
    return True 

def check_to_fit_kakao_id_rule(id):
    if check_id_length(id) and check_available_word(id) and check_dot_rule(id):
        return True
    return False

def solution(new_id):
    if check_to_fit_kakao_id_rule(new_id):
        return new_id

# check_test_case(solution("...!@BaT#*..y.abcdefghijklm"), "bat.y.abcdefghi")
# check_test_case(solution("z-+.^."), "z--")
# check_test_case(solution("=.="), "aaa")
check_test_case(solution("123_.def"), "123_.def")
# check_test_case(solution("abcdefghijklmn.p"), "abcdefghijklmn")