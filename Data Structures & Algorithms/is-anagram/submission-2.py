class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)

        for ch in t:
            if ch not in s:
                return False
            else:
                c[ch]-=1
        
        for k,v in c.items():
            if v!= 0:return False
        return True