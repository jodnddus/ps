def check_test_case(expect, result):
    if expect == result:
        print("PASS")
    else:
        print("ERR")

def get_max_value_index(number):
    return max(number)

def solution(number, k):
    answer = ""
    number = list(number)
    for i in range(len(number) - k):
        for spliced_numbers_index in range(i, (k+i)+1):
            max = 0
            current_number = number[spliced_numbers_index]
            if current_number > max:
                max = current_number
                i = spliced_numbers_index

# check_test_case(solution("1924", 2), "94")
check_test_case(solution("1231234", 3), "3234")
# check_test_case(solution("4177252841", 4), "775841")