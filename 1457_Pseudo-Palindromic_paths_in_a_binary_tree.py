from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0

        def dfs(node, path):
            nonlocal ans
            path ^= 1 << node.val
            if not node.left and not node.right:
                if not path & (path - 1):
                    ans += 1
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        dfs(root, 0)

        return ans

    def pseudoPalindromicPathsIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0

        stack = [(root, 0)]

        while stack:
            node, path = stack.pop()

            path ^= 1 << node.val

            if not node.left and not node.right:
                if not path & (path - 1):
                    ans += 1

            if node.left:
                stack.append((node.left, path))

            if node.right:
                stack.append((node.right, path))

        return ans
