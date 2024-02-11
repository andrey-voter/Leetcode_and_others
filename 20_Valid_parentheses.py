class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')', '{':'}','[':']'}

        for br in s:
            if br in d:
                stack.append(br)
            elif len(stack) == 0 or d[stack.pop()] != br:
                return False
        return len(stack) == 0
    