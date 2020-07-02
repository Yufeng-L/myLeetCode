class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        #写个更好理解的版本,但是慢一些
        l, r, s, res = 1, 2, 0, []
        while l < target / 2:
            s = sum(range(l,r+1))
            if s == target:
                res.append([i for i in range(l,r+1)])
                l += 1
            elif s < target:
                r += 1
            else:
                l += 1
        return res
        # #滑动窗口,快一些的版本
        # res = []
        # left, right, isum = 1, 1, 0
        # while(left < target / 2):
        #     #若和小于target,扩大右边界，不需要缩小左边界
        #     if isum < target:
        #         isum += right
        #         right += 1
        #     #若和大于target,缩小左边界
        #     elif isum > target:
        #         isum -= left
        #         left += 1
        #     else:
        #         #这里不是right+1的原因是在上一轮不够target的时候已经加过一次right了 正好是正确的区间
        #         tmp = [i for i in range(left,right)]
        #         res.append(tmp)
        #         isum -= left
        #         left += 1
        # return res