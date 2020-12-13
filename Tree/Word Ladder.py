class Solution:
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
