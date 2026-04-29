class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for ch in s:
            if ch.isalnum():
                a+=ch.lower()
        return a == a[::-1]