def solution_utils(diff: list) -> int:
    result = 0
    diff_len = len(diff)
    for i in range(diff_len):
        if diff[i] >= 0:
            result += diff[i]
    return result


def solution(arr: list) -> int:
    # 买卖股票最佳时机
    arr_len = len(arr)
    diff = [0] * arr_len  # 第0天, 利润为0
    for i in range(1, arr_len):
        diff[i] = arr[i] - arr[i - 1]
    result = solution_utils(diff)
    return result


if __name__ == "__main__":
    print([0] * 10)
    print("hello world")
    arr = [7, 1, 5, 10, 3, 6, 4]
    result = solution(arr)
    print(result)
