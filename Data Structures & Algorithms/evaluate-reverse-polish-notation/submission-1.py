class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ops = ["+", "-", "*", "/"]
        for ch in tokens:
            if ch not in ops:
                s.append(ch)
            else:
                b, a = s.pop(), s.pop()
                if ch == "+":
                    s.append(int(a) + int(b))
                elif ch == "-":
                    s.append(int(a) - int(b))
                elif ch == "*":
                    s.append(int(a) * int(b))
                else:
                    s.append(int(a) / int(b))
                
         
        return int(s[0])
