#leetcode46 全排列
#第一种方法直接调用itertools即可
#第二种方法回溯法
# import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #解法1
        def helper(tmp, nums):
            if not nums:
                res.append(tmp)
            else:
                for i, num in enumerate(nums):
                    helper(tmp+[num], nums[:i]+nums[i+1:])
            
        res = []
        helper([], nums)
        return res
        #解法2
        if len(nums) <= 1:
            return [nums]
        #写的比较好的回溯法
        def backtrack(nums, tmp):
            if nums == []:
                res.append(tmp[:])
            else:
                for i in range(len(nums)):
                    tmp.append(nums[i])
                    backtrack(nums[:i]+nums[i+1:], tmp)
            #若把上一行改成backtrack(nuns[:i]+nums[i+1:], tmp+[nums[i]])
            #可以省略一下三行
            if tmp == []:
                return 
            tmp.pop()
        res = []
        tmp = []
        backtrack(nums, tmp)
        return res
        #解法3
        if len(nums) <= 1:
            return [nums]
        visited = [False for _ in range(len(nums))] #记录哪些位置的元素已经访问
        res = []
        def dfs(numbers, result, cur, visit):
            if len(cur) == len(nums):
                result.append(cur[:])
                return 
            for i in range(len(nums)):
                if visit[i] == True:
                    continue
                cur.append(numbers[i])
                visit[i] = True
                dfs(numbers, result, cur, visit)
                cur.pop()
                visit[i] = False
        dfs(nums, res, [], visited)
        return res
        #解法4
        return list(itertools.permutations(nums))