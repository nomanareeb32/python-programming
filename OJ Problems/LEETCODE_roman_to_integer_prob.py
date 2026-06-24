class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000,
        }

        n = len(s)
        ptr = 0
        total = 0
        while ptr != n:
            if (ptr != n - 1):
                if roman[s[ptr + 1]] > roman[s[ptr]]:
                    total += roman[s[ptr + 1]] - roman[s[ptr]]
                    ptr += 2

                else:
                    total += roman[s[ptr]]
                    ptr += 1

            else:
                total += roman[s[ptr]]
                ptr += 1

        return total
