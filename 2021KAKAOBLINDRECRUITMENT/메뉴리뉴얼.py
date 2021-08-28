from itertools import combinations


def check_test_case(expect, result):
    if expect == result:
        print("PASS")
    else:
        print("ERR")


def count_deplicate(menu_list):
    count = {}
    for i in menu_list:
        menu_str = "".join(i)
        try:
            count[menu_str] += 1
        except:
            count[menu_str] = 1
    return count


def find_max_duplicate_menu(menu_list):
    result = []
    count = count_deplicate(menu_list)

    for i in count:
        if count[i] == max([count[order] for order in count]):
            if count[i] > 1:
                result.append(i)

    return result


def make_all_combinations(each_want_menu, menu_count):
    menus = []
    for menu in each_want_menu:
        menus.extend(list(combinations(sorted(menu), menu_count)))

    count = find_max_duplicate_menu(menus)
    return count


def solution(orders, course):
    answer = []
    for course_count in course:
        answer.extend(make_all_combinations(orders, course_count))

    return sorted(answer)


check_test_case(["AC", "ACDE", "BCFG", "CDE"], solution(
    ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))

check_test_case(["ACD", "AD", "ADE", "CD", "XYZ"], solution(
    ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))

check_test_case(["WX", "XY"], solution(["XYZ", "XWY", "WXA"], [2, 3, 4]	))
