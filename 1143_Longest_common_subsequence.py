class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                dp[i + 1][j + 1] = dp[i][j] + 1 if text1[i] == text2[j] else max(dp[i][j + 1], dp[i + 1][j])

        return dp[-1][-1]
