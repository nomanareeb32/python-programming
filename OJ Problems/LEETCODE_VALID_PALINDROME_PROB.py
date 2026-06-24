class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        l = 0
        r = len(s) - 1

        def isValid(c):
            return 'a' <= c <= 'z' or '0' <= c <= '9'

        while l <= r:
            while not isValid(s[l]):
                l += 1
                if l > r:
                    return True
            while not isValid(s[r]):
                r -= 1
                if r < l:
                    return True
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
