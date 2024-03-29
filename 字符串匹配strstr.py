#lc28
#可用find一行
#偏移表理解 find原理
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Func: 计算偏移表
        def shiftform(st):
            dic = {}
            #从后往前遍历
            for i in range(len(st)-1,-1,-1):
                if st[i] not in dic:
                    dic[st[i]] = len(st)-i
            dic["ot"] = len(st)+1
            return dic      
        # 其他情况判断
        if len(needle) > len(haystack): return -1
        if needle=="": return 0
        # 偏移表预处理    
        dic = shiftform(needle)
        idx = 0
        while idx+len(needle) <= len(haystack):
            # 待匹配字符串
            str_cut = haystack[idx:idx+len(needle)]         
            # 判断是否匹配
            if str_cut==needle:
                return idx
            else:
                # 边界处理
                if idx+len(needle) >= len(haystack):
                    return -1
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx+len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]
        return -1