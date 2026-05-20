class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        op = ('+','-','*','/')
        for ch in tokens:
            if ch not in op:
                s.append(ch)
            else:
                b,a = int(s.pop()), int(s.pop())
                if ch =='+':
                    s.append(a+b)
                elif ch =='-':
                    s.append(a-b)
                elif ch == '*':
                    s.append(a*b)
                else:
                    s.append(int(a/b))
        return int(s[0])