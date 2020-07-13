class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float("inf")
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target-s) < abs(target-res):
                    res = s
                if s < target:
                    j += 1
                    # while j < k and nums[j] == nums[j-1]: j+= 1
                elif s > target:
                    k -= 1
                    # while j < k and nums[k] == nums[k+1]: k -= 1
                else:
                    return target
        return res




