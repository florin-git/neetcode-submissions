# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # max_depth = 0

        def dfs(root, depth, max_depth):
            if not root:
                return max_depth

            max_depth = max(max_depth, depth)

            max_left = dfs(root.left, depth + 1, max_depth)
            max_right = dfs(root.right, depth + 1, max_depth)
            return max(max_left, max_right)

        return dfs(root, 1, 0)
        # return max_depth

        