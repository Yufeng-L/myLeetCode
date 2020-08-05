# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        a = self.helper(root)   # a 是一个二维数组, 为root的[偷值, 不偷值]
        return max(a)  # 返回两个值的最大值, 此值为小偷最终获得的总值
    
    # 参数为root节点, helper方法输出一个二维数组：root节点的[偷值, 不偷值]
    def helper(self, root):     # 递归结束条件：root为空, 输出 [0, 0]
        if not root:
            return [0, 0]
        left = self.helper(root.left)   # left是一个二维数组, 为 root 左侧子节点的[偷值, 不偷值]
        right = self.helper(root.right) # right也是一个二维数组, 为root右侧子节点的[偷值, 不偷值]
        robValue = left[1] + right[1] + root.val    # root 的偷值
        skipValue = max(left[0], left[1]) + max(right[0], right[1]) # root 的不偷值
        return [robValue, skipValue]    # 输出小偷可获得的最大金额
