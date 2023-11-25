import numpy as np
import pandas as pd


# 用来计算价值
def register_w(p, q):
    n = len(p)
    # 计算前缀和数组p_sum
    p_sum = [0]
    for r in range(1, n):
        p_sum.append(p[r] + p_sum[r - 1])
    # 计算前缀和数组q_sum
    q_sum = [q[0]]
    for r in range(1, n):
        q_sum.append(q[r] + q_sum[r - 1])

    def inner(i, j):
        if i == 1:
            sigma_i_j_p = p_sum[j]
            sigma_i_j_q = q_sum[j]
            return sigma_i_j_p + sigma_i_j_q
        else:
            sigma_i_j_p = p_sum[j] - p_sum[i - 1]
            sigma_i_j_q = q_sum[j] - q_sum[i - 1]
            sigma_i_j_q += q[i - 1]
            return sigma_i_j_p + sigma_i_j_q

    return inner


def opti_bst(p, q):
    n = len(p) - 1  # n表示关键字的数量, 关键字下标从1开始，本例中只有7个关键字[0 1 2 3 .. 6 7]
    w = register_w(p, q)
    e = np.full(shape=(n + 1, n + 1), fill_value=np.float32(np.inf), dtype=np.float32)
    root = np.zeros(shape=(n + 1, n + 1), dtype=np.int32)
    # 初始化, 从1到n
    for l in range(1, n + 1):
        e[l][l - 1] = q[l - 1]
    # 最后一行单独处理
    e[n][n] = q[n - 1] + q[n] + w(n, n)  # e[7][7]赋值
    # i从n-1到1
    for i in range(n - 1, 0, -1):
        # j从i到n
        for j in range(i, n + 1):
            # r从i到j
            for r in range(i, j + 1):
                if r + 1 > n:
                    continue
                temp = e[i][r - 1] + e[r + 1][j] + w(i, j)
                if temp < e[i][j]:
                    e[i][j] = temp
                    root[i][j] = r

    return e, root


if __name__ == "__main__":
    # p = [0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
    # q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
    p = [0, 0.15, 0.1, 0.05, 0.1, 0.2]
    q = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]
    w = register_w(p, q)
    e, root = opti_bst(p, q)
    print(pd.DataFrame(e))
    print("-" * 100)
    print(pd.DataFrame(root))

    print("hello world")
