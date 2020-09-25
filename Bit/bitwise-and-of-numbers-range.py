'''
https://leetcode.com/problems/bitwise-and-of-numbers-range/
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if len(bin(n))>len(bin(m)):
            return 0
        ans = m
        for num in range(m+1,n+1):
            ans = ans & num
        return ans