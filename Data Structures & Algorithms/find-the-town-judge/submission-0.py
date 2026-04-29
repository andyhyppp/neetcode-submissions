class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        c = defaultdict(int)
        t =set()
        res = []
        for a, b in trust:
            c[b] += 1
            t.add(a)
       
        for k, v in c.items():
            if v == n-1 and k not in t:
                res.append(k)

        return res[0] if len(res)==1 else -1