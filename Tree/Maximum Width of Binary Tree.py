'''
https://leetcode.com/problems/maximum-width-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        if root is None:
            return 0

        current_level = 0
        current_idx = 0
        q = deque([(root, current_level, current_idx)])

        answer = 1

        while q:
            # print(q)
            node, level, start_idx = q.popleft()

            self.bfs(q, node, level, start_idx)

            while q and q[0][1] == current_level:
                next_node, next_level, next_idx = q.popleft()
                self.bfs(q, next_node, next_level, next_idx)
                answer = max(answer, next_idx - start_idx + 1)

            current_level += 1

        return answer

    def bfs(self, q, node, level, idx):
        if node is None:
            return None
        if node.left:
            q.append((node.left, level + 1, 2 * idx + 1))
        if node.right:
            q.append((node.right, level + 1, 2 * idx + 2))
