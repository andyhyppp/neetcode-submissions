class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        res = []
        for s in strs:
            res.append(str(len(s)))
        # join lengths with comma and append '#', then concatenate strings
        encoded = ','.join(res) + '#'
        for s in strs:
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        parts = s.split('#', 1)
        length_part, rest = parts[0], parts[1] if len(parts) > 1 else ''
        if length_part == '':
            return ['' for _ in []]  # not reached in normal usage
        lengths = list(map(int, length_part.split(',')))
        res = []
        i = 0
        for l in lengths:
            res.append(rest[i:i+l])
            i += l
        return res