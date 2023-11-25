import heapq  # 可以使用元组, 这样就不会hash冲突了
import math


def dijkstra(graph: list[list], stop: list, s: int, pre: list) -> list:
    # len(pre) = num
    num = len(graph)
    d = [float("inf")] * num
    d[s] = 0
    visited: set = set()
    q: list = [(0, s)]  # 元组会对第一个元素进行比较
    while len(q) != 0:
        d_u, u = heapq.heappop(q)  # 得到最小
        visited.add(u)
        for v in range(num):
            if v in visited:
                continue
            elif d_u + graph[u][v] + stop[u] < d[v]:  # 松弛
                d[v] = d_u + graph[u][v] + stop[u]
                pre[v] = u
                heapq.heappush(q, (d[v], v))
    d = [i - stop[s] for i in d]  # 不用在出发城市滞留
    return d


def solution(n: int, m: int, stop: list[int], edges: list):
    graph = [[float("inf")] * n for _ in range(n)]
    for e in edges:
        start, end, weight = e
        graph[start - 1][end - 1] = weight
    pre = [-1] * n
    d: list = dijkstra(graph, stop, 0, pre)
    return d[n - 1]


if __name__ == "__main__":
    n = 4
    m = 4
    stop = [5, 7, 3, 4]
    edges = [(1, 2, 4), (1, 3, 5), (2, 4, 3), (3, 4, 5)]
    result = solution(n, m, stop, edges)
    print(result)
