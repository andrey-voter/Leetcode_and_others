class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) == 1:
            return 1
        left = right = 0
        ans = 0
        while right < len(chars) - 1:
            if (chars[right] != chars[right + 1]):
                len_num = right - left + 1
                chars[ans] = chars[left]
                if len_num > 1:
                    for char in str(len_num):
                        ans += 1
                        chars[ans] = char
                ans += 1
                left = right + 1
            right += 1
        chars[ans] = chars[left]
        if left == right:
            return ans + 1
        len_num = right - left + 1
        for char in str(len_num):
            ans += 1
            chars[ans] = char
        return ans + 1


S = Solution()
chars = ["a","a","a","b","b","a","a"]
print(S.compress(chars))
print(chars)
