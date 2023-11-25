import networkx as nx
import matplotlib.pyplot as plt
from collections import deque  # 双端队列, popleft, append


def draw_result(adj_matrix, flow):
    num_nodes = len(adj_matrix)
    G = nx.DiGraph()

    for i in range(num_nodes):
        G.add_node(i)

    for i in range(num_nodes):
        for j in range(num_nodes):
            if adj_matrix[i][j] != 0:
                G.add_edge(
                    i,
                    j,
                    weight="{}/{}".format(flow[i][j], adj_matrix[i][j]),
                )

    # 设置布局算法
    pos = nx.shell_layout(G)
    labels = {n: str(n) for n in G.nodes}
    nx.draw(G, pos, with_labels=True, label=labels)
    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")
    plt.title("result")
    plt.show()
    return G


class solution:
    def __init__(self, n: int, edges: list[tuple], s: int, t: int) -> None:
        self.graph = [[0] * n for _ in range(n)]
        # graph中, 反向的路径也就是正向的流量
        self.s = s
        self.t = t
        self.num = n
        for e in edges:
            start, end, weight = e
            self.graph[start][end] = weight

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

    def FordFulkson(self):
        pre = [-1] * self.num
        max_flow = 0
        while self.bfs(self.s, self.t, pre):
            path_flow = float("inf")  # 瓶颈
            s = self.t
            while s != self.s:
                path_flow = min(path_flow, self.graph[pre[s]][s])
                s = pre[s]
            max_flow += path_flow
            v = self.t
            while v != self.s:
                u = pre[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = pre[v]

        return max_flow


if __name__ == "__main__":
    edges = [
        (0, 1, 5),
        (0, 2, 4),
        (0, 3, 3),
        (1, 4, 5),
        # (4, 1, 5),
        (1, 5, 3),
        (2, 5, 3),
        (2, 6, 2),
        (3, 6, 2),
        (6, 7, 5),
        (5, 7, 3),
        (4, 7, 4),
    ]
    n = 8
    s = 0
    t = 7
    capa = [[0] * n for _ in range(n)]
    for e in edges:
        start, end, weight = e
        capa[start][end] = weight

    result = solution(n, edges, s, t)
    print("max flow: ", result.FordFulkson())

    flow = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if capa[i][j] >= 0:
                flow[i][j] = result.graph[j][i]

    draw_result(capa, flow)
    # print(capa)
    # print(flow)
