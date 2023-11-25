def partition(arr, pivot, l, r):
    # 划分，返回pivot最终的下标
    i = l
    j = r - 1
    arr[l] = None
    while (i >= j):
        while (arr[j] > pivot):
            j = j - 1
        # 右边停下了
        arr[i] = arr[j]
        arr[j] = None
        while (arr[i] < pivot):
            i = i + 1
        arr[j] = arr[i]
        arr[i] = None
    arr[i] = pivot
    return arr, i


def topK(arr, l, r, k):
    # 返回划分过后的数组和第k个数，划分后的数组还可以利用
    if l == r:
        return arr, arr[l]
    pivot = arr[l]
    arr, pivot_index = partition(arr, pivot, l, r)
    left_size = pivot_index - l + 1
    if pivot_index - l + 1 > k:
        return topK(arr, l, pivot_index, k)
    else:
        return topK(arr, pivot_index + 1, r, k - left_size)


def get_middle(arr, l, r):
    # 获得中位数，第n/2个数，并且将中位数放到l位置
    # 左右都取到的
    n = l - r + 1
    arr, arr5 = sort5(arr)
    pivot = get_middle(arr5)
    arr, pivot_index = partition(arr, pivot, l, r)
    # 如果pivot正好是中间位置
    if pivot_index == n // 2:
        return pivot
    pass


def sort5(arr):
    # 每五个进行排序
    offset = 0 if len(arr) % 5 == 0 else 1
    groups = len(arr) // 5
    arr5 = []
    for group in range(groups):
        start = group * 5
        end = (group + 1) * 5
        for i in range(start, end):
            # 从i到end中筛选出min，放到i位置
            min = arr[i]
            min_index = i
            for j in range(i, end):
                if min > arr[j]:
                    min = arr[j]
                    min_index = j
            # 交换
            arr[i], arr[min_index] = min, arr[i]
        arr5[group] = arr[start + 2]
    # 对最后一组进行单独处理
    if offset == 1:
        start = groups * 5
        end = len(arr)
        for i in range(start, end):
            min = arr[i]
            min_index = i
            for j in range(i, len(arr)):
                if min > arr[j]:
                    min = arr[j]
                    min_index = j
            arr[i], arr[min_index] = min, arr[i]
        arr5[groups] = arr[start + 2]
    # 返回已经进行排序的数组，和划分的中位数的数组
    return arr, arr5


if __name__ == '__main__':
    arr = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(arr)
