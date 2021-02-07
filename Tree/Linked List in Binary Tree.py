# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """kmp"""

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        self.lps_array, self.pattern = self.make_lps(head)
        return self.dfs(root, [])

    def dfs(self, node, res):

        if node is None:
            result = self.kmp(res)
            return result

        res.append(node.val)
        res_1 = self.dfs(node.right, res)
        res_2 = self.dfs(node.left, res)
        res.pop()
        return True if res_1 or res_2 else False

    def make_lps(self, head):

        pattern = []

        while head:
            pattern.append(head.val)
            head = head.next

        lps = [0] * len(pattern)
        ptr = 0
        for j in range(1, len(pattern)):
            while ptr and pattern[ptr] != pattern[j]:
                ptr = lps[ptr - 1]
            if pattern[ptr] == pattern[j]:
                ptr += 1
                lps[j] = ptr

        return lps, pattern

    def kmp(self, cmp):
        ptr = 0

        for i, c in enumerate(cmp):

            while ptr and self.pattern[ptr] != c:
                ptr = self.lps_array[ptr - 1]

            if self.pattern[ptr] == c:
                if ptr == len(self.pattern) - 1:
                    return True
                else:
                    ptr += 1
        return False


class Solution:
    """brute force"""

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        self.answer = self.toString(head)
        return self.dfs(root, "")

    def toString(self, head):
        ans = ""
        while head is not None:
            ans += str(head.val)
            head = head.next
        return ans

    def dfs(self, node, result):

        if result == self.answer:

            return True
        print(result)
        candidate = result + str(node.val)

        if candidate == self.answer[: len(candidate)]:
            result = candidate
        else:
            result = ""

        if node.right:
            res = self.dfs(node.right, result)
            if res:
                return True
        if node.left:
            res = self.dfs(node.left, result)
            if res:
                return True

        return False
