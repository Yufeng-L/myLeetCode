#102 二叉树的层序遍历 BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []  # 特殊情况，root为空直接返回
        from collections import deque
        # 下面就是BFS模板内容，BFS关键在于队列的使用
        layer = deque()
        layer.append(root)  # 压入初始节点
        res = []  # 结果集
        while layer:
            cur_layer = []  # 临时变量，记录当前层的节点
            for _ in range(len(layer)):  # 遍历某一层的节点
                node = layer.popleft()  # 将要处理的节点弹出
                cur_layer.append(node.val)
                if node.left:  # 如果当前节点有左右节点，则压入队列，根据题意注意压入顺序，先左后右，
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            res.append(cur_layer)  # 某一层的节点都处理完之后，将当前层的结果压入结果集
        return res

#DFS:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.level(root, 0, res)
        return res

    def level(self, root, level, res):
        if not root: return
        if len(res) == level: 
        	res.append([])
        res[level].append(root.val)
        if root.left: self.level(root.left, level + 1, res)
        if root.right: self.level(root.right, level + 1, res)

#144 二叉树的前序遍历
# preorder(root,left,right)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, output = [root], []
        # 不能像层序遍历一样，用stack的话可以保证最后一个处理的肯定是左子树，右子树最后处理
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        
        return output

#94 二叉树的中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res

#145 二叉树的后序遍历
#结果是为反向的BFS
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, res = [root],[]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]




