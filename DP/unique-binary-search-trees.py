"""
https://leetcode.com/problems/unique-binary-search-trees/submissions/
"""


class Solution:
    """Using Definition of Catalan"""

    def numTrees(self, n: int) -> int:
        return int(comb(2 * n, n) / (n + 1))


class Solution:
    """General Solution"""

    def numTrees(self, n: int) -> int:

        if n == 1:
            return 1
        self.dp = [1] * (n + 1)

        self.dp[0] = 1
        self.dp[1] = 1
        self.dp[2] = 2

        for i in range(3, n + 1):
            cnt = 0
            for j in range(1, i + 1):
                cnt += self.dp[j - 1] * self.dp[i - j]
            self.dp[i] = cnt
        return self.dp[-1]


class Solution:

    """Symmetric Solution"""

    def numTrees(self, n: int) -> int:

        if n == 1:
            return 1
        self.dp = [1] * (n + 1)

        self.dp[0] = 1
        self.dp[1] = 1
        self.dp[2] = 2

        for i in range(3, n + 1):
            cnt = 0
            half = i // 2
            for j in range(1, half + 1):
                cnt += self.dp[j - 1] * self.dp[i - j]
            if i % 2 == 0:
                self.dp[i] = 2 * cnt
            else:
                self.dp[i] = 2 * cnt + self.dp[i // 2] * self.dp[i // 2]
        return self.dp[-1]
