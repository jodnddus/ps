def solution(n, lost, reserve):
    for rsv in reserve:
        if len(lost) == 0:
            break

        try:
            a = lost.index(rsv+1)
            b = lost.index(rsv-1)

            


solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
