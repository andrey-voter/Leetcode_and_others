from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        key_value = defaultdict(int)
        key_value[0] = 1
        prefix_sum = ans = 0

        for num in nums:
            prefix_sum += num

            ans += key_value[prefix_sum - k]
            key_value[prefix_sum] += 1

        return ans
