#剑指offer38 个人觉得理解有点困难 在于for-loop开始dfs的顺序
#参考: https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/
class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c)) # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i] # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1) # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i] # 恢复交换
        dfs(0)
        return res

class Solution:
    def permutation(self, s: str) -> List[str]:
        def helper(tmp ,s):
            if not s:
                res.append(''.join(tmp))
            for i,c in enumerate(s):
                helper(tmp+[c], s[:i]+s[i+1:])
        res = []
        charlist = list(s)
        helper([], charlist)
        return list(set(res))

