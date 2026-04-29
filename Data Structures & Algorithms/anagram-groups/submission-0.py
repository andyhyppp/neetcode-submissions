class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter

        d = defaultdict(list)
        for i in strs:
            count = [0]*26
            for ch in i:
                count[ord(ch)-ord('a')]+=1
            d[tuple(count)].append(i)
        return d.values()
            