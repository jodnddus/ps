from test import check_test_case


def search(depth, k, dungeons):
    depths = [depth]
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            spare_dungeons = dungeons.copy()
            del spare_dungeons[i]
            depths.append(search(depth + 1, k - dungeons[i][1], spare_dungeons))

    return max(depths)


def solution(k, dungeons):
    return search(1, k, dungeons)


check_test_case(solution(80, [[80, 20], [50, 40], [30, 10]]), 3)
