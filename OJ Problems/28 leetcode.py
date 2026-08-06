class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = needle[0]
        for i in range(len(haystack)):
            if haystack[i] == b:
                if haystack[i:i + a] == needle:
                    return i
        return -1