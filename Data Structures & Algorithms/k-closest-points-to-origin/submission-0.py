class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        def dist(x,y):
            return (x**2+ y**2)**0.5
        
        arr = []
        for x,y in points:
            arr.append((dist(x,y), (x,y)))
        
        heapq.heapify(arr)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(arr)[1])
        return ans