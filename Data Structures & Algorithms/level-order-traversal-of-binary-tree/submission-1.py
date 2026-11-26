# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        # second val is the level
        q = deque([[root, 1]])

        while q:
            cur, lev = q.popleft()

            if len(res) != lev:
                res.append([])

            res[lev - 1].append(cur.val)
            if cur.left:
                q.append([cur.left, lev + 1])
            if cur.right:
                q.append([cur.right, lev + 1])

        return res
