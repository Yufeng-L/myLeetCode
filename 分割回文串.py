class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def helper(tmp, s):
            if not s:
                res.append(tmp)
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    helper(tmp + [s[:i]], s[i:])
        helper([], s)
        return res

