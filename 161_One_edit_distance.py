class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False

        if len(s) == len(t):
            i = 0
            error_cnt = 0
            while i < len(s):
                if s[i] != t[i]:
                    error_cnt += 1
                    if error_cnt > 1:
                        return False
                i += 1
            if error_cnt == 0:
                return False
            return True

        if len(s) < len(t):
            s, t = t, s

        error_flag = 0

        for i in range(len(t)):
            if t[i] == s[i + error_flag]:
                continue

            if error_flag:
                return False

            error_flag = 1
            if t[i] != s[i + 1]:
                return False

        return True


S = Solution()
s = input()
t = input()
print(S.isOneEditDistance(s, t))
