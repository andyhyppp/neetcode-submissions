[1,1,2,8,]
[48,24,6, 1]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r =[],[]
        a = 1

        for i in range(len(nums)):
            l.append(a)
            a*=nums[i]
        a = 1
        for i in range(len(nums)-1,-1,-1):
            r.append(a)
            a*=nums[i]
        r = r[::-1]
        res =[]
        for i in range(len(l)):
            res.append(l[i]*r[i])
        return res
