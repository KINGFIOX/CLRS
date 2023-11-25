import collections


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        num_freq = collections.Counter(nums)
        self.res = []
        xfs = list(num_freq.items())
        xfn = len(xfs)
        self.quick_sort(xfs, 0, xfn - 1, k)
        return self.res

    def quick_sort(self, xfs, l: int, r: int, k: int) -> None:
        pivot_xf = xfs[l]
        pivot_f = xfs[l][1]
        idx = l
        for i in range(l + 1, r + 1, 1):
            if xfs[i][1] >= pivot_f:
                idx += 1
                xfs[idx], xfs[i] = xfs[i], xfs[idx]
        xfs[l], xfs[idx] = xfs[idx], xfs[l]

        if k == idx - l + 1:
            for i in range(l, idx + 1):
                self.res.append(xfs[i][0])
        elif k < idx - l + 1:
            self.quick_sort(xfs, l, idx - 1, k)
        else:
            for i in range(l, idx + 1):
                self.res.append(xfs[i][0])
            self.quick_sort(xfs, idx + 1, r, k - (idx - l + 1))


if __name__ == "__main__":
    print("hello world")
