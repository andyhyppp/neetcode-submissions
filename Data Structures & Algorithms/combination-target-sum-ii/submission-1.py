class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()            # also sort if you need uniqueness
        ans = []

        def bt(s, i, temp):
            # 1) If I've hit the target, record and stop exploring this branch
            if s == target and temp not in ans:
                ans.append(temp)
                return
            # 2) If I've overshot or run out of numbers, stop
            if s > target or i >= len(nums):
                return

            # 3) Otherwise, try including nums[i], then excluding it
            bt(s + nums[i], i + 1, temp + [nums[i]])
            bt(s,             i + 1, temp)

        bt(0, 0, [])
        return ans