class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for k,i in enumerate(nums):
            if i in seen.keys():
                return [seen[i], k]
            else:
                seen[target-i] = k
        return -1