class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        self.n = len(grid)
        self.grid = grid
        self.memo = {}
        return max(self.dfs(0, 0, 0, 0), 0)

    def dfs(self, rx, ry, lx, ly):

        if rx > self.n - 1 or ry > self.n - 1 or lx > self.n - 1 or ly > self.n - 1:
            return -float("inf")
        if (rx, ry, lx, ly) in self.memo.keys():
            return self.memo[(rx, ry, lx, ly)]

        if self.grid[rx][ry] == -1 or self.grid[lx][ly] == -1:
            self.memo[(rx, ry, lx, ly)] = -float("inf")
            return -float("inf")

        if rx == self.n - 1 and ry == self.n - 1:
            return self.grid[rx][ry]

        if lx == self.n - 1 and ly == self.n - 1:
            return self.grid[lx][ly]

        cherries = 0
        if rx == lx and ry == ly:
            cherries += self.grid[rx][ry]
        else:
            cherries += self.grid[rx][ry] + self.grid[lx][ly]

        cherries += max(
            self.dfs(rx + 1, ry, lx + 1, ly),
            self.dfs(rx + 1, ry, lx, ly + 1),
            self.dfs(rx, ry + 1, lx + 1, ly),
            self.dfs(rx, ry + 1, lx, ly + 1),
        )
        self.memo[(rx, ry, lx, ly)] = cherries
        return cherries