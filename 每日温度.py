class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 可以维护一个存储下标的单调栈，从栈底到栈顶的下标对应的温度列表中的温度依次递减。
        # 如果一个下标在单调栈里，则表示尚未找到下一次温度更高的下标。
        res = [0] * len(T)
        stack = [] #栈存的是元素的下标 单调栈
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:    # 栈不为空 && 栈顶温度小于当前温度
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res