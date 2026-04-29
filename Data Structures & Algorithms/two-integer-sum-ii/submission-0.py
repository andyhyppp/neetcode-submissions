class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for k,v in enumerate(numbers):
            diff = target - v
            if diff in d:
                return [d[diff]+1, k+1]
            else:
                d[v] = k
        return 