import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy
from sympy import isprime
from collections import deque  # 双端队列, popleft, append


class solution:
    def __init__(self, n: int, arr: list[int]) -> None:
        # arr就是存放的待匹配的数
        self.num = n + 2
        self.graph: list[list] = [[0] * self.num for _ in range(self.num)]
        # 只是用作测试
        self.arr: list = deepcopy(arr)
        self.prime: list = [i for i in self.arr if isprime(i)]
        self.not_prime: list = [i for i in self.arr if not isprime(i)]
        self.contain2: bool = 2 in self.arr
        if self.contain2:
            self.prime.remove(2)
        # 画图
        self.G = nx.DiGraph()
        self.G.add_node("dummy_s")  # 起点
        self.G.add_node("dummy_t")  # 终点
        for i in range(1, self.num - 1):
            self.G.add_node(arr[i - 1])
        # dummy_s = 0; dummy_s = n + 1

    def draw_graph(self, capa: list, residual: list):
        len_prime = len(self.prime)
        len_not = len(self.not_prime)
        for i in range(len_prime):
            for j in range(len_not):
                trans_i = i + 1
                trans_j = j + 1 + len_prime
                if capa[trans_i][trans_j] > 0:
                    self.G.add_edge(
                        self.prime[i],
                        self.not_prime[j],
                        weight="{}/{}".format(
                            capa[trans_i][trans_j] - residual[trans_i][trans_j],
                            capa[trans_i][trans_j],
                        ),
                    )
        for i in range(len_prime):
            trans_i = 1 + i
            self.G.add_edge(
                "dummy_s",
                self.prime[i],
                weight="{}/{}".format(
                    capa[0][trans_i] - residual[0][trans_i],
                    capa[0][trans_i],
                ),
            )
        for j in range(len_not):
            trans_j = 1 + len_prime + j
            self.G.add_edge(
                self.not_prime[j],
                "dummy_t",
                weight="{}/{}".format(
                    capa[trans_j][self.num - 1] - residual[trans_j][self.num - 1],
                    capa[trans_j][self.num - 1],
                ),
            )

        pos = nx.shell_layout(self.G)
        labels = {n: str(n) for n in self.G.nodes}
        nx.draw(self.G, pos, with_labels=True, label=labels)
        edge_labels = {(u, v): d["weight"] for u, v, d in self.G.edges(data=True)}
        nx.draw_networkx_edge_labels(
            self.G, pos, edge_labels=edge_labels, font_color="red"
        )
        plt.title("result")
        plt.show()

    def handle(self):
        if self.contain2:
            self.prime_couple(True)
            capa1 = deepcopy(self.graph)
            ans1: int = self.FordFulkson(0, self.num - 1)
            residual1 = deepcopy(self.graph)
            self.prime.remove(2)

            self.graph = [[0] * self.num for _ in range(self.num)]  # 重置

            self.prime_couple(False)
            capa2 = deepcopy(self.graph)
            ans2: int = self.FordFulkson(0, self.num - 1)
            residual2 = deepcopy(self.graph)
            self.not_prime.remove(2)

            if ans1 > ans2:
                self.prime.append(2)
                self.draw_graph(capa1, residual1)
                return ans1
            else:
                self.not_prime.append(2)
                self.draw_graph(capa2, residual2)
                return ans2
        else:
            self.prime_couple(False)
            capa = deepcopy(self.graph)
            ans: int = self.FordFulkson(0, self.num - 1)
            residual = deepcopy(self.graph)
            self.draw_graph(capa, residual)
            return ans

    def prime_couple(self, prime_have_two: bool):
        # 是否要让prime数组中有2
        if self.contain2:
            if prime_have_two:  # 让prime中加入2
                self.prime.append(2)
                len_prime = len(self.prime)
                len_not = len(self.not_prime)
                for i in range(len_prime):
                    for j in range(len_not):
                        trans_i = i + 1
                        trans_j = j + 1 + len_prime
                        if isprime(self.prime[i] + self.not_prime[j]):
                            self.graph[trans_i][trans_j] = 1
            else:
                self.not_prime.append(2)
                len_prime = len(self.prime)
                len_not = len(self.not_prime)
                for i in range(len_prime):
                    for j in range(len_not):
                        trans_i = i + 1
                        trans_j = j + 1 + len_prime
                        if isprime(self.prime[i] + self.not_prime[j]):
                            self.graph[trans_i][trans_j] = 1
        else:
            len_prime = len(self.prime)
            len_not = len(self.not_prime)
            for i in range(len_prime):
                for j in range(len_not):
                    trans_i = i + 1
                    trans_j = j + 1 + len_prime
                    if isprime(self.prime[i] + self.not_prime[j]):
                        self.graph[trans_i][trans_j] = 1
        # 将dummy_s->"素数"->"非素数“连接起来
        for i in range(len(self.prime)):
            trans_i = 1 + i
            self.graph[0][trans_i] = 1
        for j in range(len(self.not_prime)):
            trans_j = len(self.prime) + 1 + j
            self.graph[trans_j][self.num - 1] = 1

    def bfs(self, s: int, t: int, pre: list) -> bool:
        # 能从s到达t, 那么就返回true
        visited = [0] * self.num
        m_q = deque()
        m_q.append(s)
        visited[s] = True

        while len(m_q) != 0:
            u = m_q.popleft()
            for v in range(self.num):
                if not visited[v] and self.graph[u][v] > 0:
                    m_q.append(v)
                    visited[v] = True
                    pre[v] = u
                    if v == t:
                        return True
        return False

    def FordFulkson(self, s, t):
        pre = [-1] * self.num
        max_flow = 0
        while self.bfs(s, t, pre):
            path_flow = float("inf")  # 瓶颈
            u = t
            while u != s:
                path_flow = min(path_flow, self.graph[pre[u]][u])
                u = pre[u]
            max_flow += path_flow
            v = t
            while v != s:
                u = pre[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = pre[v]

        return max_flow


if __name__ == "__main__":
    n = 4
    arr = [2, 5, 6, 13]
    result = solution(n, arr)
    ans = result.handle()
    print(ans)

# if __name__ == "__main__":
#     edges = [
#         (0, 1, 5),
#         (0, 2, 4),
#         (0, 3, 3),
#         (1, 4, 5),
#         # (4, 1, 5),
#         (1, 5, 3),
#         (2, 5, 3),
#         (2, 6, 2),
#         (3, 6, 2),
#         (6, 7, 5),
#         (5, 7, 3),
#         (4, 7, 4),
#     ]
#     n = 8
#     s = 0
#     t = 7
#     capa = [[0] * n for _ in range(n)]
#     for e in edges:
#         start, end, weight = e
#         capa[start][end] = weight

#     result = solution(8, [2, 4])
#     result.graph = copy.deepcopy(capa)
#     print("max flow: ", result.FordFulkson(0, 7))
#     print(result.prime)
#     print(result.not_prime)
#     print(result.contain2)

#     flow = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if capa[i][j] >= 0:
#                 flow[i][j] = result.graph[j][i]

#     draw_result(capa, flow)
#     # print(capa)
#     # print(flow)
