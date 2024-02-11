class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(s: str, left: int, right: int):
            if left + right == 2 * n:
                res.append(s)
                return
            if left < n:
                generate(s + '(', left + 1, right)
            if right < left:
                generate(s + ')', left, right + 1)

        generate("", 0, 0)
        return res
