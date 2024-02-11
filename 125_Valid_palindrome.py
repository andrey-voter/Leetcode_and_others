class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right > 0 and not s[right].isalnum():
                right -= 1
            if left > right:
                return True

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


# A bit more beautiful variant:
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


# S = Solution()
# s = "A man, a plan, a canal: Panama"
# print(S.isPalindrome(s))
