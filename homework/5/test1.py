import heapq
import random


class activity:
    def __init__(self, s: int, f: int, i: int) -> None:
        self.s = s
        self.f = f
        self.i = i  # 这个i表示标号

    def __lt__(self, other) -> bool:
        return self.s > other.s

    def __str__(self) -> str:
        return f"i: {self.i}\ts: {self.s}\tf: {self.f}"


def is_compatible(a: activity, b: activity) -> bool:
    if a.s <= b.s and a.f <= b.s:
        # a在b之前, 并且a与b相容
        return True
    if b.s <= a.s and b.f <= a.s:
        return True
    return False


def solution_utils(act_arr: list) -> list:
    result = []
    heapq.heapify(act_arr)  # 建堆
    last = heapq.heappop(act_arr)
    result.append(last)
    while act_arr:
        i = heapq.heappop(act_arr)
        last = result[-1]
        if is_compatible(last, i):
            result.append(i)
    result.reverse()
    return result


def solution(s_arr: list, f_arr: list) -> list:
    act_len: int = len(s_arr)
    act_arr: list = [
        activity(s, t, i) for (s, t, i) in zip(s_arr, f_arr, range(act_len))
    ]
    random.shuffle(act_arr)
    result = solution_utils(act_arr)
    return result


if __name__ == "__main__":
    s_arr: list = [3, 1, 5, 2, 5, 3, 8, 6, 8, 12]
    f_arr: list = [6, 4, 7, 5, 9, 8, 11, 10, 12, 14]
    result = solution(s_arr, f_arr)
    for i in result:
        print(i)
    print("hello world")
