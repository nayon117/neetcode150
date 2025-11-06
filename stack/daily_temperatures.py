class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res
