class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        cur_length = prev_length = ans = 0
        for c in nums:
            if c == 1:
                cur_length += 1
            else:
                ans = max(ans, cur_length + prev_length)
                prev_length = cur_length
                cur_length = 0
        ans = max(ans, cur_length + prev_length)
        return ans - 1 if ans == len(nums) else ans

