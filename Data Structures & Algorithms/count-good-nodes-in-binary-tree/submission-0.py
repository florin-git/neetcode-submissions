# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0

        def dfs(cur, max_val):
            nonlocal res

            if not cur:
                return

            if cur.val >= max_val:
                res += 1

            max_val = max(max_val, cur.val)
            dfs(cur.left, max_val)
            dfs(cur.right, max_val)

        dfs(root, root.val)
        return res
        