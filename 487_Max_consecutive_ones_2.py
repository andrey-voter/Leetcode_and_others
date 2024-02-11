class Solution:
    def findMaxConsecutiveOnes(self, s: list[int]) -> int:
        ans = prev = cur = 0
        for c in s:
            if c == 0:
                ans = max(ans, prev + cur + 1)
                prev = cur
                cur = 0
            else:
                cur += 1
        ans = max(ans, prev + cur + 1)
        return ans


arr = [int(num) for num in input().split()]
print(Solution().findMaxConsecutiveOnes(arr))
