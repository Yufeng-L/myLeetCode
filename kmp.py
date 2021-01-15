def KMP(string, pattern):
    '''
    KMP字符串匹配的主函数
    若存在字串返回字串在字符串中开始的位置下标，或者返回-1
    '''
    pnext = gen_pnext(pattern)
    n = len(string)
    m = len(pattern)
    i, j = 0, 0
    while (i<n) and (j<m):
        if (string[i]==pattern[j]):
            i += 1
            j += 1
        elif (j!=0):
            j = pnext[j-1]
        else:
            i += 1
    if (j == m):
        return i-j
    else:
        return -1
            
    
def gen_pnext(pattern):
    """
    构造临时数组pnext
    """
    # ji
    # aabbaac
    j, i, m = 0, 1, len(pattern)
    pnext = [0] * m
    while i < m:
        if pattern[i] == pattern[j]:
            pnext[i] = j + 1
            i += 1
            j += 1
        elif j != 0:
            j = pnext[j - 1]
        else:
            pnext[j] = 0
            i += 1
    return pnext

 
if __name__ == "__main__":
    string = 'abcxabcdabcdabcy'
    pattern = 'abcdabcy'
    out = KMP(string, pattern)
    print(out)