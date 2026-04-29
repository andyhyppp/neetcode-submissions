class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def bt(s,i,temp=[]):
            if s >target or i>=len(nums):
                return
            elif s == target:
                ans.append(temp)
            else:
                bt(s+nums[i], i, temp+[nums[i]])
                bt(s, i+1, temp)

        bt(0,0,[])
        return ans