
'''
https://leetcode.com/problems/invert-binary-tree/
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''bfs solution'''
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = [root]
        if not root:
            return root
        while queue:
            node = queue.pop(0)
            self.swap(node)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
                
        return root
            
    def swap(self,node):
        tmp = node.left
        node.left = node.right
        node.right = tmp