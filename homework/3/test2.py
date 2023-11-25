def bin_search_utils(arr, l, r, target):
    # base case
    if l == r:
        return l
    elif l > r:
        return -1
    mid = l + ((r - l) >> 2)
    if arr[mid] > target:
        # 在左边找
        return bin_search_utils(arr, l, mid - 1, target)
    elif arr[mid] < target:
        return bin_search_utils(arr, mid + 1, r, target)
    else:
        # 如果相等，剪枝
        return mid


def bin_search(arr, target):
    # 防御
    if arr == None or len(arr) == 0:
        return -1
    return bin_search_utils(arr, 0, len(arr) - 1, target)


if __name__ == '__main__':
    arr = [-1, 0, 3, 5, 9, 12]
    target = 2
    index = bin_search(arr, target)
    print(index)
