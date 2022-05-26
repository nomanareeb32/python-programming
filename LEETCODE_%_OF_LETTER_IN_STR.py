class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        a = s.count(letter)
        return (a*100)//len(s)