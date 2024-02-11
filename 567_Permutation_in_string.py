from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter = Counter(s1)
        n_match = 0

        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -= 1
                if counter[s2[i]] == 0:
                    n_match += 1
            if i >= len(s1):
                if s2[i - len(s1)] in counter:
                    if counter[s2[i - len(s1)]] == 0:
                        n_match -= 1
                    counter[s2[i - len(s1)]] += 1
            if n_match == len(counter):
                return True

        return False


s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))
