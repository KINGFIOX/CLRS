def solution(arr: list) -> int:
    arr_len: list = len(arr)
    if arr_len == 0:
        return -1
    if arr_len == 1:
        return 0  # 不用跳跃了
    result: int = 0
    curDistance: int = 0  # 当前步覆盖范围
    nextDistance: int = arr[0] + 1  # 下一步覆盖范围
    for i in range(arr_len):
        nextDistance = max(arr[i] + 1, nextDistance)
        if i == curDistance:
            result += 1
            curDistance = nextDistance
            if nextDistance >= arr_len - 1:
                break

    return result


if __name__ == "__main__":
    arr = [2, 3, 1, 1, 4]
    result = solution(arr)
    print(result)
    print("hello world")
