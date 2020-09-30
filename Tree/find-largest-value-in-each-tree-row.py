"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
515. Find Largest Value in Each Tree Row
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
Example 2:

Input: root = [1,2,3]
Output: [1,3]
Example 3:

Input: root = [1]
Output: [1]
"""


class MySolution:
    def largestValues(self, root: TreeNode) -> List[int]:
        """using level index"""

        if root is None:
            return []

        queue = [(root, 0)]
        cnt = 0
        ans = [root.val]

        while len(queue) > 0:

            node, level = queue.pop(0)
            if len(ans) < level + 1:
                ans.append(node.val)
            else:
                if ans[level] < node.val:
                    ans[level] = node.val
            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))

        return ans


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        '''using size of level'''
        
        if root is None:
            return []
        
        queue = [root]
        cnt = 0 
        answer = []
        
        while len(queue)>0:
            size = len(queue)
            max_value_row = -float('inf')
            for i in range(size):
                node = queue.pop(0)
                if node.val>max_value_row:
                    max_value_row = node.val
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            answer.append(max_value_row)
                
        return answer