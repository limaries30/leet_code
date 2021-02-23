# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.topDown(root))

    def topDown(self, node):

        if node is None:
            return (0, 0)

        leftMax, rightMax = self.topDown(node.left), self.topDown(node.right)

        now = node.val + leftMax[1] + rightMax[1]
        later = max(leftMax) + max(rightMax)

        return (now, later)
