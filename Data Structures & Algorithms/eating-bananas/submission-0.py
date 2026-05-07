class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        
        def helper(x):
            a = 0
            for p in piles:
                a += p//x
                if p%x!=0:
                    a+=1
            return a

    
        while l<r:
            m = (l+r)//2
            if helper(m)<=h:
                r = m 
            else:
                l = m+1

        return l
        
    


