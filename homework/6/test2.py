import heapq
import random


class A_star:
    def __init__(self, num_epochs: int, map: list[list[float]]) -> None:
        self.num_epochs: int = num_epochs
        self.map = map  # 用二维数组来存储图
        self.num = len(map)  # 有多少个节点
        self.all_bitmap: str = "1" * self.num  # 用来记录全部节点的位图
        self.path: list = []  # 用来搜集结果
        self.cost: float = float("inf")  # 代价
        self.handle()
        self.path.reverse()

    def handle(self):
        root_index: int = random.randint(0, self.num - 1)  # 随机产生一个出发的节点
        # root_index = 0
        root_node: node = node(self.map, root_index, "0" * self.num, 0, None)
        my_heap: list[node] = []
        heapq.heappush(my_heap, root_node)
        epoch: int = 0
        while len(my_heap) != 0:
            cur_node: node = heapq.heappop(my_heap)
            cur_index: int = cur_node.index
            if cur_node.bitmap == self.all_bitmap:
                if epoch >= self.num_epochs:
                    return
                else:
                    epoch += 1
                temp_cost: float = cur_node.g + self.map[cur_index][root_index]
                # 到叶节点了, 搜集结果
                if self.cost > temp_cost:
                    del self.path
                    self.path: int = []
                    self.cost = temp_cost
                    self.path.append(root_index)
                    self.path.append(cur_index)
                    parent_node: node = cur_node.parent
                    while parent_node != None:
                        parent_index = parent_node.index
                        self.path.append(parent_index)
                        parent_node = parent_node.parent
            else:
                rest_index: list[int] = [
                    c for c in range(self.num) if cur_node.bitmap[c] == "0"
                ]  # 剩余的下标
                # 没有到叶子节点
                for next_index in rest_index:
                    next_node_g: float = self.map[cur_index][next_index] + cur_node.g
                    next_node: node = node(
                        self.map, next_index, cur_node.bitmap, next_node_g, cur_node
                    )
                    heapq.heappush(my_heap, next_node)  # 插入堆中


class node:
    # 搜索树上的节点的结构体
    def __init__(
        self, map: list[list[float]], index: int, bitmap: str, g: float, parent
    ) -> None:
        self.index = index  # 当前节点的下标
        bitmap_list = list(bitmap)
        bitmap_list[self.index] = "1"
        self.bitmap: str = "".join(bitmap_list)  # 位图, 用来存储已经遍历的节点(包含当前节点)
        self.g: float = g  # 已有代价
        self.parent = parent  # 搜索树的, 当前节点的父节点(谁产生他的)
        self.num = len(self.bitmap)  # 有多少节点
        self.f = self.get_f(map)  # f = g + h

    def __lt__(self, other):
        return self.f < other.f

    def get_f(self, map: list[list[float]]):
        rest = [c for c in range(self.num) if self.bitmap[c] == "0"]  # 没有被访问过节点
        arr = map[self.index]
        h = float("inf")
        for i in rest:
            if arr[i] < h:
                h = arr[i]
        return self.g + h + len(rest) - 1


if __name__ == "__main__":
    test_map = [
        [float("inf"), 10, 15, 20, 25],
        [10, float("inf"), 35, 25, 20],
        [15, 35, float("inf"), 30, 10],
        [20, 25, 30, float("inf"), 50],
        [25, 20, 10, 50, float("inf")],
    ]
    test_a_star = A_star(1, test_map)
    print(test_a_star.cost)
    print(test_a_star.path)
