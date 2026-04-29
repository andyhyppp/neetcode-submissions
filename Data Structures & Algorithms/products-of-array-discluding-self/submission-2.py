class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        s = 1
        for i in range(len(nums)):
            l.append(s)
            s = s * nums[i]
        s = 1
        for i in range(len(nums)-1,-1,-1):
            l[i] *= s
            s = s*nums[i]
        return l