class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)

        while l<r:
            m = (l+r)>>1
            if nums[m]<nums[0]:
                r = m
            else:
                l = m+1
        return nums[l] if l<len(nums) else nums[0]