#show raw.where(block: true) : block.with(
  fill: luma(240),
  inset: (x: 3pt, y: 0pt),
  outset: (y: 3pt),
  radius: 2pt,
)

= 思路

定义一个数组, 叫做 "增量"(利润).
利润数组"diff[i] = arr[i] - arr[i-1]".
股票当天的市价 - 股票前一天的市价.

利润只要是正的, 那么就赚钱了, 因此, 只要 "diff[i] >= 0",
那么就搜集结果

```py
def solution_utils(diff: list) -> int:
    result = 0
    diff_len = len(diff)
    for i in range(diff_len):
        if diff[i] >= 0:
            result += diff[i]
    return result


def solution(arr: list) -> int:
    # 买卖股票最佳时机
    arr_len = len(arr)
    diff = [0] * arr_len  # 第0天, 利润为0
    for i in range(1, arr_len):
        diff[i] = arr[i] - arr[i - 1]
    result = solution_utils(diff)
    return result


if __name__ == "__main__":
    print([0] * 10)
    print("hello world")
    arr = [7, 1, 5, 10, 3, 6, 4]
    result = solution(arr)
    print(result)
```

== 第二题思路

如果只能买卖两次, 那么是不能使用 "贪心算法" 的

反例: `arr = [2, 4, 1, 5, 6, 3]`, 那么`diff = [0, 2, -3, 4, 1, -3]`

这次我们贪心, 选取最大的两个利润, 得到的`result = 2 + 4 = 6`

但实际上, 我们可以`arr[4] - arr[0] = 6 - 2 = 4` + `arr[3] - arr[2] = 5 - 1 = 4`, 结果`result = 8`