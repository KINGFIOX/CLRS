# 找两个数组第k小的，m+n是奇数
def find_k_smallest(arr1, arr2, k):
    if not arr1:
        return arr2[k - 1]
    if not arr2:
        return arr1[k - 1]
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    if k == 1:
        return min(arr1[0], arr2[0])
    # 查找第k/2小的数
    i = min(len(arr1), k >> 1)
    j = min(len(arr2), k >> 1)
    if arr1[i - 1] < arr2[j - 1]:
        arr1 = arr1[i:]
        return find_k_smallest(arr1, arr2, k - i)
    else:
        arr2 = arr2[j:]
        return find_k_smallest(arr1, arr2, k - j)


def find_mid(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    if (((m + n) >> 1) << 1) == (m + n):
        # 如果是偶数
        mid_low = find_k_smallest(arr1, arr2, (m + n) >> 1)
        mid_high = find_k_smallest(arr1, arr2, ((m + n) >> 1) + 1)
        return (mid_low + mid_high) / 2
    else:
        # 如果是奇数
        mid_high = find_k_smallest(arr1, arr2, ((m + n) >> 1) + 1)
        return mid_high


if __name__ == "__main__":
    arr1 = [1, 2, 5]
    arr2 = [3, 4, 6]
    print(find_mid(arr1, arr2))
