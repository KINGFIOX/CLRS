from collections import deque  # 双端队列, append, appendleft, pop, popleft
import math


def spfa(graph: list[list], s: int, k: int) -> list:
    # s 是 源点
    # 只对经过路径不超过k的时松弛
    num = len(graph)
    path_len = [0] * num  # 路径的长度不超过k
    d = [float("inf")] * num  # 初始化距离
    d[s] = 0
    q = deque()  # 初始化双端队列
    q.append(s)
    while len(q) != 0:
        u = q.popleft()
        if path_len[u] >= k:
            continue
        else:
            for v in range(num):  # 遍历邻居
                if path_len[v] >= k:
                    continue
                elif d[u] + graph[u][v] < d[v]:
                    d[v] = d[u] + graph[u][v]  # 松弛
                    path_len[v] = path_len[u] + 1
                    if not v in q:
                        q.append(v)
                    if d[q[-1]] < d[q[0]]:  # 优化, 较小者优先
                        temp = q.popleft()
                        q.append(temp)

    # 判断是否有负环, 最后一轮松弛
    for i in range(num):
        if path_len[i] >= k:
            continue
        else:
            for j in range(num):
                if path_len[j] >= k:
                    continue
                elif d[i] + graph[i][j] < d[j]:
                    return None

    return d


def solution(n: int, m: int, k: int, edges: list):
    # m条边, n个节点, 路径最多是k
    # edges中的元素是(start, end, weight)
    graph = [[float("inf")] * n for _ in range(n)]
    for e in edges:
        start, end, weight = e
        graph[start - 1][end - 1] = weight
    d = spfa(graph, 0, k)
    if d == None:
        print("imposible")
    elif math.isinf(d[n - 1]):
        print("imposible")
    else:
        print(d[n - 1])


if __name__ == "__main__":
    n = 3
    m = 3
    k = 1
    edges = [(1, 2, 1), (2, 3, 1), (1, 3, 3)]
    solution(n, m, k, edges)
