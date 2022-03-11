from test import check_test_case


def dfs(sum, nums, index, sums_array):
    if (len(nums) == index):
        sums_array.append(sum)
        return
    else:
        dfs(sum + nums[index], nums, index + 1, sums_array)
        dfs(sum - nums[index], nums, index + 1, sums_array)

    return sums_array


def solution(numbers, target):
    sums_array = dfs(0, numbers, 0, [])
    print(sums_array, len(sums_array))
    return sums_array.count(target)


check_test_case(solution([1, 1, 1, 1, 1], 3), 5)
check_test_case(solution([4, 1, 2, 1], 4), 2)
