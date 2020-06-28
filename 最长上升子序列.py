#Leetcode300

# nums = [10,2,5,3,108,11]
#         j  i
#   dp = [1, 1, 1, 1, 1, 1]
#若 nums[i]> nums[j] 则 dp[i]要比dp[j]+1
#初始化dp数组全部为1

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

