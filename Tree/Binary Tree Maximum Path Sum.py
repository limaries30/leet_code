"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        self.max_val = -float("inf")
        self.dfs(root)
        return self.max_val

    def dfs(self, root):
        if root is None:
            return 0

        left_sum = max(0, self.dfs(root.left))
        right_sum = max(0, self.dfs(root.right))

        self.max_val = max(self.max_val, root.val + left_sum + right_sum)

        return root.val + max(left_sum, right_sum)
