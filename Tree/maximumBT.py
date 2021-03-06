'''
https://leetcode.com/problems/maximum-binary-tree/
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        ans = self.make(nums)
        
        return ans
        
                    
    def make(self,arr):
        
        if len(arr)==0:
            return None

        
        parent = max(arr)
        idx = arr.index(parent)

        parentNode = TreeNode(val=parent)
        
        parentNode.left = self.make(arr[:idx])    
        parentNode.right = self.make(arr[idx+1:])
            
        return parentNode
            
        