from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l is inclusive, r is exclusive [l, r)
        l, r = 0, len(nums)

        while l < r:
            m = (l + r) >> 1

            # 1. Since r = m and l = m + 1 both exclude m, 
            # we MUST check if m is the target right now.
            if nums[m] == target:
                return m

            # 2. Is the left half sorted?
            if nums[l] <= nums[m]:
                
                # Is the target strictly in this left half?
                # (We already know it's not m, so we use < instead of <=)
                if nums[l] <= target < nums[m]:
                    r = m       # m is excluded from the new right bound
                else:
                    l = m + 1   # m is excluded from the new left bound
                    
            # 3. Otherwise, the right half is sorted
            else:
                
                # Is the target strictly in this right half?
                # NOTE: Because r is exclusive, the last valid element is at r - 1
                if nums[m] < target <= nums[r - 1]:
                    l = m + 1   # m is excluded
                else:
                    r = m       # m is excluded

        # If the loop finishes and we haven't returned m, it's not in the array
        return -1