class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ans = []
        left = right = 0
        while right < len(nums) - 1:
            if nums[right] + 1 != nums[right + 1]:
                ans.append(f"{nums[left]}" if left == right else f"{nums[left]}->{nums[right]}")
                left = right + 1
            right += 1
        if left >= right or len(nums) == 1:
            ans.append(f"{nums[left]}")
        else:
            ans.append(f"{nums[left]}->{nums[right]}")
        return ans
