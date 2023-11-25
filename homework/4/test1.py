import numpy as np


def knapsack_dim2(w, v, capacity):
    n = len(v)
    dp = np.zeros(shape=(n, capacity + 1), dtype=np.int32)
    for j in range(capacity + 1):
        if j >= w[0]:
            dp[0][j] = v[0] + dp[0][j - w[0]]
    for i in range(1, n):
        for j in range(1, capacity + 1):
            if j >= w[i]:
                dp[i][j] = max(dp[i - 1][j], v[i] + dp[i][j - w[i]])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)
    return dp[n - 1][capacity]


def knapsack_dim1(w, v, capacity):
    n = len(v)
    dp = np.zeros(shape=(capacity + 1), dtype=np.int32)
    for i in range(0, n):
        for j in range(w[i], capacity + 1):
            dp[j] = max(dp[j], v[i] + dp[j - w[i]])
    print(dp)
    return dp[capacity]


if __name__ == "__main__":
    w = [1, 2, 3, 4]
    v = [2, 4, 4, 5]
    capacity = 5
    result1 = knapsack_dim1(w, v, capacity)
    print(result1)
    result2 = knapsack_dim2(w, v, capacity)
    print(result2)
