class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dic = {')':'(', '}':'{', ']':'['}
        for ch in s:
            if ch in dic:
                if st and st[-1] == dic[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        return st==[] 