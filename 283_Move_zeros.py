class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for num in nums:
            if num:
                nums[pos] = num
                pos += 1
        nums[pos:] = [0] * len(nums[pos:])
    