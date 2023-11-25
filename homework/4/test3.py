import numpy as np


def process(nums):
    n = len(nums)
    dp = np.zeros(shape=n, dtype=np.int32)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[n - 1]


def kill_mice(arr):
    # 掐头
    arr1 = arr[1:]
    # 去尾
    arr2 = arr[:-1]
    return max(process(arr1), process(arr2))


if __name__ == "__main__":
    arr = [1, 2, 3, 1]
    ans = kill_mice(arr)
    print(ans)
