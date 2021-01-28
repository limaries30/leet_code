class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        """fails why?"""

        visited = [0] * len(A)
        dummy_visited = [0] * len(A)
        cnt = 0
        current_cycle = ""

        for adx, a in enumerate(A):

            if not visited[adx]:
                visited[adx] = 1
                next_char = B[adx]
                next_adx = 0
                current_cycle = a + next_char
                while next_char != a:

                    next_adx = self.find(next_char, A, visited)
                    prev_char = next_char
                    next_char = B[next_adx]
                    visited[next_adx] = 1

                    if next_char == prev_char:
                        continue

                    if next_char in current_cycle and next_char != a:

                        pair = self.find(next_char, current_cycle, dummy_visited)
                        print(current_cycle[pair:])
                        cnt += len(current_cycle[pair:]) - 1
                        current_cycle = current_cycle[: pair + 1]
                    else:
                        current_cycle += next_char
            if len(current_cycle) == 0:
                continue

            cnt += len(current_cycle) - 2
            current_cycle = ""
        return cnt

    def find(self, target, obj, visited):

        for idx, c in enumerate(obj):
            if c == target and not visited[idx]:
                return idx
