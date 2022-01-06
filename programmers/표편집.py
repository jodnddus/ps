# https://programmers.co.kr/learn/courses/30/lessons/81303
# 이중연결리스트
from test import check_test_case


class Node:
    def __init__(self):
        self.num = 0
        self.removed = False
        self.prev = None
        self.next = None


def solution(n, k, cmds):
    list = [Node() for _ in range(n)]
    stack = []
    for i in range(1, n):
        list[i].num = i
        list[i-1].next = list[i]
        list[i].prev = list[i-1]

    current = list[k]

    for cmd in cmds:
        if cmd[0] == "U":
            amount = int(cmd.split(" ")[1])
            for _ in range(amount):
                current = current.prev
        elif cmd[0] == "D":
            amount = int(cmd.split(" ")[1])
            for _ in range(amount):
                current = current.next
        elif cmd[0] == "C":
            stack.append(current.num)
            current.removed = True

            if current.prev:
                current.prev.next = current.next

            if current.next:
                current.next.prev = current.prev
                current = current.next
            else:
                current = current.prev
        elif cmd[0] == "Z":
            pop = stack.pop()
            restore = list[pop]
            restore.removed = False

            if restore.prev:
                restore.prev.next = restore
            if restore.next:
                restore.next.prev = restore

    answer = ''
    for item in list:
        if item.removed:
            answer += 'X'
        else:
            answer += 'O'

    return answer


check_test_case(solution(
    8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]), "OOOOXOOO")
check_test_case(solution(8, 2, [
                "D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]), "OOXOXOOO")
