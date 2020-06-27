# #Leetcode3 defaultdict解法
s = "abcabcaa"

from collections import defaultdict

l, ans = 0,0
counter = defaultdict(lambda:0)
for r in range(len(s)):
	# 若此时遍历的元素之前遍历过(不等于0)
	while counter.get(s[r],0) != 0:
		print("s[l] is: ", s[l])
		print("counter[s[l]] is ", counter[s[l]])
		# counter[s[l]] = counter.get(s[l],0) - 1
		counter[s[l]] -= 1
		l += 1
	counter[s[r]] += 1
	ans = max(ans, r - l + 1)

print(counter)
print(ans)

#较好理解的version
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        if not s: return 0
        cur, res, left = 0, 0, 0
        lookup = set()
        #若需要print, 增加start, end用于标注位置
        start, end = 0, 0
        for i in range(len(s)):
        	cur += 1
        	while s[i] in lookup:
        		lookup.remove(s[left])
        		left += 1
        		cur -= 1
        	if cur >= res:
        		res = cur
        		#用于找到所属字符串
        		end = i
        		start = i - res + 1
        	lookup.add(s[i])
        print(s[start: end+1])
        return res

if __name__ == "__main__":
	sol = Solution()
	s = "abcccdbqc"
	print(sol.lengthOfLongestSubstring(s))