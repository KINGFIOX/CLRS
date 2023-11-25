import math


def insertion_sort(arr, start, end):
    # 从小到大排序
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            # 腾出位置
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def partition(arr, low, high):
    # 返回位置
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def heapify(arr, n, i):
    # 从上到下调整
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # 找到大的孩子
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    # 交换
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    # 堆排序
    n = len(arr)
    # 从后到前，堆排序
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def intro_sort(arr):
    # 闭区间
    size = len(arr)
    intro_sort_util(arr, 0, size - 1, 2 * math.log2(size))


def intro_sort_util(arr, begin, end, depth_limit):
    size = end - begin
    if size < 16:
        # 小于16个元素，那么插入排序
        insertion_sort(arr, begin, end)
    elif depth_limit == 0:
        # 如果递归深度只有0
        heap_sort(arr[begin: end + 1])
    else:
        pivot = partition(arr, begin, end)
        intro_sort_util(arr, begin, pivot - 1, depth_limit - 1)
        intro_sort_util(arr, pivot + 1, end, depth_limit - 1)
