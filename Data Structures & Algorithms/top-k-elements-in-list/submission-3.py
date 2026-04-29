class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort counter
        count = Counter(nums)
        return sorted(count, key=lambda x: -count[x])[:k]
