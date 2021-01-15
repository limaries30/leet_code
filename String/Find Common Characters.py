"""
https://leetcode.com/problems/find-common-characters/

Q) How to solve in O(N)?
"""


class Solution:
    """O(N) using hash"""

    def commonChars(self, A: List[str]) -> List[str]:
        result = [float("inf") for i in range(26)]
        answer = []

        for a in A:
            cnt = self.hash_cnt(a)
            for j in range(26):
                result[j] = min(result[j], cnt[j])

        for i in range(26):
            if result[i] > 0:
                for j in range(result[i]):
                    answer.append(chr(i + ord("a")))
        return answer

    def hash_cnt(self, word):
        cnt = [0 for i in range(26)]
        for w in word:
            cnt[ord(w) - ord("a")] += 1

        return cnt


class Solution:
    """O(NMlogM)"""

    def commonChars(self, A: List[str]) -> List[str]:

        word = list(A[0])

        for w in A[1:]:
            new_word = []
            for c in w:
                if c in word:
                    idx = word.index(c)
                    new_word.append(word.pop(idx))
            word = new_word
        return new_word