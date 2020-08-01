class Solution:
    #1.迭代
    def subsets(self, nums: List[int]) -> List[List[int]]:     
        res = [[]]
        for i in nums:
            res += [[i] + num for num in res]
        return res
        
    #2.库函数
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res
    #3.递归
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res