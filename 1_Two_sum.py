class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {int: int}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [i, d[target - nums[i]]]
            d[nums[i]] = i
