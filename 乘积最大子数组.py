class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        imax, imin = 1, 1
        for num in nums:
            #若当前数 < 0, imax和imin要先互换
            if num < 0:
                imax, imin = imin, imax
            imax = max(imax * num, num)
            imin = min(imin * num, num)
            res = max(imax, res)
        return res