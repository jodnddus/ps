# https://programmers.co.kr/learn/courses/30/lessons/67256

left = [1, 4, 7]
right = [3, 6, 9]
middle = [2, 5, 8, 0]

kp = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    '*': (3, 0), 0: (3, 1), '#': (3, 2)
}


def calc_distance(number, cur_position):
    return abs(kp[number][0] - kp[cur_position][0]) + abs(kp[number][1] - kp[cur_position][1])


def choose_neer_finger(number, hand, cur_left, cur_right):
    left_distance = calc_distance(number, cur_left)
    right_distance = calc_distance(number, cur_right)

    if left_distance > right_distance:
        return 'R'
    elif right_distance > left_distance:
        return 'L'
    else:
        if hand == 'left':
            return 'L'
        else:
            return 'R'


def choose_finger(number, hand, cur_left, cur_right):
    if number in left:
        return 'L', number
    elif number in right:
        return 'R', number
    else:
        return choose_neer_finger(number, hand, cur_left, cur_right), number


def solution(numbers, hand):
    answer = ''
    cur_left = '*'
    cur_right = '#'

    for number in numbers:
        moved_hand, number = choose_finger(number, hand, cur_left, cur_right)

        if moved_hand == 'L':
            cur_left = number
        elif moved_hand == 'R':
            cur_right = number

        answer += moved_hand

    return answer


def check_test_case(expect, result):
    if expect == result:
        print("PASS")
    else:
        print("ERR")


check_test_case(
    solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"), 'LRLLLRLLRRL')
check_test_case(
    solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"), 'LRLLRRLLLRR')
check_test_case(
    solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"), 'LLRLLRLLRL')
