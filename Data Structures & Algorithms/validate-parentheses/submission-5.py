class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', '}': '{', ']' : '['}

        stack = []

        for ch in s:
            if ch in d.keys():
                if not stack or d[ch] != stack.pop():
                    return False

            else:
                stack.append(ch)
        
        return stack == []