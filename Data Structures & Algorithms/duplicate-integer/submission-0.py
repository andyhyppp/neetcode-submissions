class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        for k,v in c.items():
            if v>1:
                return True

        return False