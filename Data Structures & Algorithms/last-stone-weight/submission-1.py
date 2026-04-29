class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-w for w in stones]
        heapq.heapify(s)

        while len(s)>1:
            x, y= heapq.heappop(s), heapq.heappop(s)
            if x == y:
                continue
            else:
                heapq.heappush(s, -abs(y-x))

        return s[0]*-1 if s else 0