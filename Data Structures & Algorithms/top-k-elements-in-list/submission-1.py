class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq


        c = Counter(nums)
        d = [(-v,k) for k,v in c.items()]
        heapq.heapify(d)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(d)[1])
        return res