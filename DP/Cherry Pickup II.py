"""'https://leetcode.com/problems/cherry-pickup-ii/"""


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.memo = {}
        self.grid = grid
        self.n_rows = len(grid)
        self.n_cols = len(grid[0])
        return self.step(0, 0, 0, self.n_cols - 1)

    def step(self, rx, ry, lx, ly):
        if (rx, ry, lx, ly) in self.memo.keys():
            return self.memo[(rx, ry, lx, ly)]
        if ry < 0 or ly < 0 or ry >= self.n_cols or ly >= self.n_cols:
            return -float("inf")
        if rx == self.n_rows - 1:
            if ly == ry:
                return self.grid[rx][ry]
            else:
                return self.grid[rx][ry] + self.grid[lx][ly]
        cherries = 0
        if rx == lx and ry == ly:
            cherries = self.grid[rx][ry]
        else:
            cherries = self.grid[rx][ry] + self.grid[lx][ly]
        next_cherries = -float("inf")
        for j in range(-1, 2):
            for i in range(-1, 2):
                next_cherries = max(next_cherries, self.step(rx + 1, ry + i, lx + 1, ly + j))

        # print(rx,ry,lx,ly,cherries,next_cherries)
        res = cherries + next_cherries
        self.memo[(rx, ry, lx, ly)] = res
        return res