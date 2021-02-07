# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        result = []
        
        if root is None:
            return result
        
        self.cnt = {}
        self.subtree_sum(root)
        sorted_x = sorted(self.cnt.items(), key=lambda kv: kv[1],reverse=True)
        max_cnt = sorted_x[0][1]

        for x in sorted_x:
            if x[1]==max_cnt:
                result.append(x[0])
            else:
                break
        return result
    
    def subtree_sum(self,node):
        
        
        if node is None:
            return 0
        current_subtree_sum = node.val
        current_subtree_sum += self.subtree_sum(node.left)
        current_subtree_sum += self.subtree_sum(node.right)
        self.count(current_subtree_sum)
        return current_subtree_sum
    
    def count(self,val):
        if val in self.cnt.keys():
            self.cnt[val]+=1
        else:
            self.cnt[val]=1