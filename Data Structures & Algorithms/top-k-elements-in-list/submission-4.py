class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # minheap
        import heapq

        count=Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)