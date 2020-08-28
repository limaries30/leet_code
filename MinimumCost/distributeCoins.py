'''
https://leetcode.com/problems/distribute-coins-in-binary-tree/
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.
'''

class Solution:
    
    def distributeCoins(self, root: TreeNode) -> int:
        
        self.cnt = 0
        self.move(root)
        
        return self.cnt
        
    def move(self,node):
        
        if node is None:
            return 0
        
        right_child = self.move(node.right)
        left_child = self.move(node.left)
        
        self.cnt = self.cnt + abs(right_child)+abs(left_child)
        
        node.val =  right_child+left_child + node.val
        
        return node.val-1
        