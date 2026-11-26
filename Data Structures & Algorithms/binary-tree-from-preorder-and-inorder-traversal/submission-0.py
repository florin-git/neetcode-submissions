# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder: visit, left, right
        # inorder: left, visit, right

        # preorder traversal has the root in first position
        # for preorder root + all left children + all right children
        # for inorder, all left children + root + all right children
        # the leftmost node in preorder is the first node in inorder

        # index in inorder indicates the leftmost node so far

        # when leftmost is reached inorder index + 1 and go up to prev,
        # then you create right child of this node

        # find the root in inorder from preorder idx = 0
        # build the root
        # call the operation on the left and update preorder idx + 1
        # call the operation on the right and update preorder idx + 1

        # if just one element return the node

        positions = {}
        for i, n in enumerate(inorder):
            positions[n] = i

        preorder_idx = [-1]

        def build_tree_recursively(l, r):
            if r < l:
                return None

            preorder_idx[0] += 1
            root_val = preorder[preorder_idx[0]]
            root = TreeNode(val=root_val)
            root_idx = positions[root_val]

            root.left = build_tree_recursively(l, root_idx - 1)
            root.right = build_tree_recursively(root_idx + 1, r)

            return root

        return build_tree_recursively(0, len(inorder) - 1)












