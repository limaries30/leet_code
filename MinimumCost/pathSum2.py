'''
https://leetcode.com/problems/path-sum-ii/
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.sum = sum
        self.ans = []
        if root is None:
            return None
        self.DFS(root,[root.val])
        return self.ans
        
    def DFS(self,node,result):

        if sum(result) == self.sum and not node.right and not node.left:
            self.ans.append(result)
            return
        if node.left:
            left_res = self.CopyAppend(result,node.left.val)
            self.DFS(node.left,left_res)
        if node.right:
            right_res = self.CopyAppend(result,node.right.val)
            self.DFS(node.right,right_res)
            
    def CopyAppend(self,li,x):
        res = copy.copy(li)
        res.append(x)
        return res