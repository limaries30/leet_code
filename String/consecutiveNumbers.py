"""
829. Consecutive Numbers Sum
Hard

429

553

Add to List

Share
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
"""


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # n*b + n(n+1)/2 = N
        # b = N/n-(n+1)/2

        cnt = 0
        for n in range(1, int((math.sqrt(1 + 8 * N) - 1) / 2 + 1)):
            b = N / n - (n + 1) / 2
            if b.is_integer():
                cnt += 1
        return cnt
