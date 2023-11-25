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


def top_k_frequent_elements(arr, k):
    # 频数
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    fre_value = frequency.values()
    kth_value = bfprt(arr, len(fre_value) - k + 1)
    # 划分
    ans_value = [value for value in fre_value if value >= kth_value]
    ans_key = []
    for key, value in frequency.items():
        if value in ans_value:
            ans_key.append(key)

    return ans_key


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 4, 4, 4, 5, 5]
    nums = [1]
    k = 1
    ans = top_k_frequent_elements(nums, k)
    print(ans)
