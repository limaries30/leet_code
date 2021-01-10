"""
https://leetcode.com/problems/string-without-aaa-or-bbb/
"""


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        return self.main("a", "b", a, b) if a > b else self.main("b", "a", b, a)

    def main(self, big_word, small_word, big, small):

        if big == 2 * small:
            return (big_word * 2 + small_word) * small
        if big > 2 * small:
            return (big_word * 2 + small_word) * small + big_word * (big - 2 * small)
        if 2 * small > big:
            return (big_word * 2 + small_word) * (big - small) + (big_word + small_word) * (
                2 * small - big
            )
