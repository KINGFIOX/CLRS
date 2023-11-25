def compute_prefix(pattern: str):
    m: int = len(pattern)
    pi: list = [0] * (m + 1)  # pi[0..m]
    # 第m位置是虚拟位置
    for q in range(2, m + 1):  # 第q个位置失配
        k = pi[q - 1]
        while k > 0 and pattern[k] != pattern[q - 1]:  # 找到最长的前后缀的, 前缀位置
            k = pi[k]
        if pattern[k] == pattern[q - 1]:
            k = k + 1
        pi[q] = k
    # print(pi, len(pi))
    return pi


def search(pattern: str, match: str):
    m: int = len(pattern)
    n: int = len(match)
    arr: list = []
    pi = compute_prefix(pattern)
    q = 0
    for i in range(0, n):
        while q > 0 and pattern[q] != match[i]:
            q = pi[q]
        if pattern[q] == match[i]:
            q = q + 1
        if q == m:  # 匹配成功
            arr.append(i - m + 1)
            q = pi[q]
    return arr


if __name__ == "__main__":
    match = "sadbutsad"
    pattern = "sad"
    # arr1 = "abaabaababab"
    # arr2 = "abmnab56abmnabkfghabmnab56abmnab"
    pi = compute_prefix(pattern)

    found = search(pattern=pattern, match=match)
    if len(found) == 0:
        print(-1)
    else:
        print(found)
