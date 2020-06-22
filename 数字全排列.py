#leetcode46 全排列
#第一种方法直接调用itertools即可
#第二种方法回溯法
# import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        visited = [False for _ in range(len(nums))] #记录哪些位置的元素已经访问
        res = []
        def dfs(numbers, result, cur, visit):
            if len(cur) == len(nums):
                result.append(cur[:])
                return 
            for i in range(len(nums)):
                #如果已访问则跳到下一个
                if visit[i] == True:  
                    continue
                cur.append(numbers[i])
                #设置成已访问
                visit[i] = True
                dfs(numbers, result, cur, visit)
                #恢复到之前状态
                cur.pop()
                visit[i] = False
        dfs(nums, res, [], visited)
        return res
        
        # return list(itertools.permutations(nums))