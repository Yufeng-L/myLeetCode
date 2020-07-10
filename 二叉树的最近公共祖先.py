# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    	#递归
    	#if not root: return None (此时root == None, 合并为返回None)
    	#if root == p or root == q: return root
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return 
        #若left为None,返回right
        if not left: return right
        #同理
        if not right: return left 
        return root