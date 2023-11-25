import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


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


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


# 创建最优二叉搜索树
# 接收的root是一个二维数组
def set_opti_bst(root, i, j, keys):
    # base case
    if i > j:
        return None
    if i == j:
        k = keys[i]
        n = Node("k" + str(k))
        n.left = Node("d" + str(k - 1))
        n.right = Node("d" + str(k))
        return n
    # 根节点
    r = root[i][j]
    k = keys[r]
    n_root = Node("k" + str(k))
    n_left = set_opti_bst(root, i, r - 1, keys)
    n_right = set_opti_bst(root, r + 1, j, keys)
    if n_left == None:
        n_left = Node("d" + str(k - 1))
        n_root.left = n_left
    else:
        n_root.left = n_left
    if n_right == None:
        n_right = Node("d" + str(k))
        n_root.right = n_right
    else:
        n_root.right = n_right

    return n_root


def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.value] = (x, y)
    if node.left:
        G.add_edge(node.value, node.left.value)
        l_x, l_y = x - 1 / 2**layer, y - 1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
    if node.right:
        G.add_edge(node.value, node.right.value)
        r_x, r_y = x + 1 / 2**layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
    return (G, pos)


def draw(node):  # 以某个节点为根画图
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()


def opti_bst(p, q):
    n = len(p) - 1  # 一共有7个关键字
    w = register_w(p, q)
    e = np.full((n + 1 + 1, n + 1), fill_value=np.inf, dtype=np.float32)
    root = np.zeros((n + 1, n + 1), dtype=np.int32)

    for l in range(0, n + 2):  # 从1到8初始化，多了一行，为了防止出现越界的情况
        e[l][l - 1] = q[l - 1]

    # i从n到1
    for i in range(n, 0, -1):
        # j从1到n
        for j in range(i, n + 1):
            # r从i到j
            for r in range(i, j + 1):
                temp = e[i][r - 1] + e[r + 1][j] + w(i, j)
                if temp < e[i][j]:
                    e[i][j] = temp
                    root[i][j] = r

    return e, root


if __name__ == "__main__":
    p = [0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
    q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
    keys = [0, 1, 2, 3, 4, 5, 6, 7]
    # p = [0, 0.15, 0.1, 0.05, 0.1, 0.2]
    # q = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]
    w = register_w(p, q)
    e, root = opti_bst(p, q)
    print(pd.DataFrame(e))
    print("-" * 100)
    print(pd.DataFrame(root))
    node = set_opti_bst(root, 1, len(keys) - 1, keys)
    draw(node)
