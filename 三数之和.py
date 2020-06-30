#Leetcode 15 mid
# 双指针
# [1, 2, 3, 4, 5]
#  k->i->    <-j
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        k = 0
        for k in range(len(nums)-2):
            #因为数组已排序,若最小的都大于0直接返回空数组
            if nums[k] > 0: break 
            #首先固定k
            if k > 0 and nums[k] == nums[k - 1]: continue
            #初始化i为k的后一位,向右移动
            i = k + 1
            #j为数组的最后一位,向左移动
            j = len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
                else:
                    res.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
        return res