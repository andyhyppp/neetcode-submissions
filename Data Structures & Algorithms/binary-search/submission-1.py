class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n

        while l < r:
            m = (r - l) // 2 + l
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return r if r < n and nums[r] == target else -1
