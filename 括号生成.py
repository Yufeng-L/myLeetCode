class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        tmp = ""
        def helper(tmp, left, right):
            if left > right:
                return 
            if right == 0:
                res.append(tmp)
            if left > 0:
                helper(tmp+'(', left-1, right)
            if right > 0:
                helper(tmp+')', left, right-1)
        helper(tmp, n, n)
        return res

            