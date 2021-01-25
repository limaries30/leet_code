'''
https://leetcode.com/problems/word-ladder/submissions/
그래프를 만들면 더 좋을듯!
'''
class Solution:
    '''bi-directional bfs'''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        self.len_word = len(beginWord)
        self.wordList = wordList

        start = {"deq": deque([(beginWord, 1)]), "history": set([beginWord])}
        end = {"deq": deque([(endWord, 1)]), "history": set([endWord])}
        current_level = 1

        if endWord not in wordList:
            return 0

        while len(start["deq"]) > 0 or len(end["deq"]) > 0:

            if self.bfs(start, end, current_level):
                return 2 * current_level
            if self.bfs(end, start, current_level):
                return 2 * current_level + 1
            current_level += 1

        return 0

    def bfs(self, q, other, level):
        deq = q["deq"]
        history = q["history"]
        opposite_hisotry = other["history"]

        while deq and deq[0][1] == level:
            word, cnt = deq.popleft()
            for w in self.wordList:
                if w not in history and self.compare(word, w):
                    if w in opposite_hisotry:
                        return True
                    deq.append((w, level + 1))
                    history.add(w)
        return False

    def compare(self, word_1, word_2):

        cnt = 0
        for i in range(self.len_word):
            if word_1[i] != word_2[i]:
                cnt += 1
                if cnt > 1:
                    return False
        return True if cnt == 1 else False


class Solution:
    """bfs"""

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        self.len_word = len(beginWord)
        self.deq = deque()
        self.history = set()
        self.wordList = wordList

        self.add2deq(beginWord, 1)

        while len(self.deq) > 0:

            word, cnt = self.deq.popleft()

            if word == endWord:
                return cnt
            self.add2deq(word, cnt)

        return 0

    def compare(self, word_1, word_2):

        cnt = 0
        for i in range(self.len_word):
            if word_1[i] != word_2[i]:
                cnt += 1
                if cnt > 1:
                    return False
        return True if cnt == 1 else False

    def add2deq(self, word, cnt):

        for w in self.wordList:
            if w not in self.history and self.compare(word, w):
                self.deq.append((w, cnt + 1))
                self.history.add(w)
