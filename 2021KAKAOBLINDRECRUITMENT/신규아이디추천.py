import re

def check_test_case(expect, result):
    if expect == result:
        print("PASS")
    else:
        print("ERR")

def is_below_min_length(length):
    if length <= 15:
        return True
    return False

def is_over_max_length(length):
    if length >= 3:
        return True
    return False

def check_id_length(id):
    id_length = len(id)
    if is_below_min_length(id_length) and is_over_max_length(id_length):
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
    if result or id[0] == '.' or id[len(id)-1] == '.':
        return False 
    return True 

def check_to_fit_kakao_id_rule(id):
    if check_id_length(id) and check_available_word(id) and check_dot_rule(id):
        return True
    return False

def change_lower_case(id):
    return id.lower()

def delete_not_available_word(id):
    return re.sub(r"[^0-9a-z\-\_\.]", "", id)

def change_dot(id):
    return re.sub(r"\.{2,}", ".", id)

def delete_dot_first_last(id):
    return re.sub(r"^\.|\.$", "", id)

def add_a_if_none(id):
    if id == '':
        return "a"
    return id

def slice_id_over_length(id):
    if not is_below_min_length(id): 
        # TODO 여기서부터
        # new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
        # if 제거 후 마침표(.)가 new_id의 끝에 위치한다면
        # 끝에 위치한 마침표(.) 문자를 제거합니다.

def solution(new_id):
    if check_to_fit_kakao_id_rule(new_id):
        return new_id

# check_test_case(solution("...!@BaT#*..y.abcdefghijklm"), "bat.y.abcdefghi")
# check_test_case(solution("z-+.^."), "z--")
# check_test_case(solution("=.="), "aaa")
check_test_case(solution("123_.def"), "123_.def")
# check_test_case(solution("abcdefghijklmn.p"), "abcdefghijklmn")