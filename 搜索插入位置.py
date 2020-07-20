class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
        # if target < nums[0] or not nums:
        #     return 0
        # if target > nums[-1]:
        #     return len(nums)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #     elif nums[i+1] > target:
        #         return i+1
