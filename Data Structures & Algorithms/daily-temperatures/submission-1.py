class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0]* len(temperatures)
        for k, v in enumerate(temperatures):
            while s and v > temperatures[s[-1]]:
                i = s.pop()
                res[i] = k-i
            s.append(k)
        return res    