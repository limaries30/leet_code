"""
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        if len(preorder) == 1 and preorder != "#":
            return False

        inner_stack = []
        outer_stack = list(preorder.split(","))

        while outer_stack:
            node = outer_stack.pop(0)
            while inner_stack and node == inner_stack[-1] == "#":
                inner_stack.pop()
                if len(inner_stack) == 0:
                    return False
                inner_stack.pop()
            inner_stack.append(node)
        return inner_stack == ["#"]
