# https://programmers.co.kr/learn/courses/30/lessons/81303
from test import check_test_case


def solution(n, k, cmds):
    answer = ['O' for _ in range(n)]
    original = [n for n in range(n)]
    table = original.copy() 
    removes = []

    for cmd in cmds:
        if cmd[0] == "U":
            k -= int(cmd[2])
        elif cmd[0] == "D":
            k += int(cmd[2])
        elif cmd[0] == "C":
            removes.append(table.copy())
            del table[k]
        elif cmd[0] == "Z":
            old_table = removes.pop()
            table = old_table

    for num in set([n for n in range(n)]) - set(table):
        answer[num] = 'X'

    return "".join(answer)


check_test_case(solution(
    8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]), "OOOOXOOO")
check_test_case(solution(8, 2, [
                "D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]), "OOXOXOOO")
