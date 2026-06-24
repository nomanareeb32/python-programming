class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less_target = 0
        n_target = 0
        for value in nums:
            if value < target:
                less_target += 1
            if value == target:
                n_target += 1

        result = [less_target + i for i in range(n_target)]
        return result


