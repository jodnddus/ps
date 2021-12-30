# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    if n == 1:
        return "수"

    if n % 2 == 0:
        return "수박" * int(n / 2)
    else:
        return "수박" * int(n / 2) + "수"


solution(4)
solution(3)
