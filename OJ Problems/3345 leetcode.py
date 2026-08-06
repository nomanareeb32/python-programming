class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            individual_digits = [int(i) for i in str(n)]
            product = 1
            for j in individual_digits:
                product *= j
            if product % t == 0:
                return n
            n += 1