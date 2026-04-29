class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        s = 1
        for i in range(len(nums)):
            res.append(s)
            s = s * nums[i]
        s = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= s
            s = s*nums[i]
        return res