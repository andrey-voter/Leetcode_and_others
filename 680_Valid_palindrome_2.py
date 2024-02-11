class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                variant_1 = s[left: right]
                variant_2 = s[left + 1: right + 1]
                return variant_1 == variant_1[::-1] or variant_2 == variant_2[::-1]
            left += 1
            right -= 1
        return True


s = "abca"
print(Solution().validPalindrome(s))
