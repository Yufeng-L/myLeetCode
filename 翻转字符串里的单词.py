class Solution:
    def reverseWords(self, s: str) -> str:
        #解法1 双指针
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i+1:j+1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)
        #解法2 使用Split()去掉任意whitespace
        # a = s.split()
        # return ' '.join(a[::-1])
