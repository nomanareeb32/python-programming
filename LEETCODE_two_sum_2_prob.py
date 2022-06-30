class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            if nums[i] in a:
                index = a.index(nums[i])
                return [index + 1, i + 1]

            else:
                a.append(target - nums[i])
