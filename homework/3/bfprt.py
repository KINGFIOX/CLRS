def bfprt(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = select_pivot(arr)
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]
    if k <= len(left):
        return bfprt(left, k)
    elif k > len(left) and k <= len(left) + len(equal):
        return equal[0]
    else:
        return bfprt(right, k - len(left) - len(equal))


def select_pivot(arr):
    if len(arr) <= 5:  # 中间位置
        return sorted(arr)[len(arr) >> 1]
    chunks = chunked(arr, 5)
    full_chunks = [chunk for chunk in chunks if len(chunk) == 5]  # 完整的chunk
    sorted_groups = [sorted(chunk) for chunk in full_chunks]  # 给长度为5的chunk排序
    medians = [chunk[2] for chunk in sorted_groups]  # 这个是中位数的集合
    median_of_medians = bfprt(medians, len(medians) >> 2)  # 中之王者
    return median_of_medians


def chunked(iterable, n):  # 将n个打包成一个数组，在放到一个二维数组中
    return [iterable[i:i + n] for i in range(0, len(iterable), n)]


def middle_k(arr, k):
    n = len(arr)
    n_div_2 = n >> 1
    mid = bfprt(arr, n_div_2)
    print(mid)
    bucket = []
    ans = []
    for i in range(n):
        bucket.append(abs(arr[i] - mid))
    ret = bfprt(bucket, k)
    for i in range(n):
        temp = abs(arr[i] - mid)
        if temp <= ret:
            ans.append(arr[i])
    return ans


if __name__ == "__main__":
    # 示例
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    ans = middle_k(arr, 3)
    print(ans)
