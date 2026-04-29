class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            c = 1
            while num +1 in nums:
                num+=1
                c+=1
            ans = max(ans,c)
        return ans