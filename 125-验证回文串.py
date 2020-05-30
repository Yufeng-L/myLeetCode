#Leetcode125 
#一个字符串，判断是否回文，包括大小写字母和数字，大小写等价。
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^\w\d]','',s)
        s = s.lower()
        if s == s[::-1]:
            return True
        return False