"""
https://leetcode.com/problems/01-matrix/
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """bfs start from (1)=>slow"""
        self.matrix = matrix
        self.n_row = len(matrix)
        self.n_col = len(matrix[0])
        self.answer = [[0 for i in range(self.n_col)] for j in range(self.n_row)]

        for x in range(self.n_row):
            for y in range(self.n_col):
                self.BFS(x, y)
        return self.answer

    def get_next(self, pos):

        x, y = pos
        next_positions = list(
            filter(
                lambda x: x[0] >= 0 and x[0] < self.n_row and x[1] >= 0 and x[1] < self.n_col,
                [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]],
            )
        )
        return next_positions

    def BFS(self, x, y):
        queue = [[x, y]]

        while len(queue) > 0:
            node_x, node_y = queue.pop(0)
            if self.matrix[node_x][node_y] == 0:
                self.answer[x][y] = abs(x - node_x) + abs(y - node_y)
                return

            next_nodes = self.get_next([node_x, node_y])
            queue.extend(next_nodes)


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """bfs starting from target(0)=>faster"""
        self.matrix = matrix
        self.n_row = len(matrix)
        self.n_col = len(matrix[0])
        queue = []
        visited = set()

        for x in range(self.n_row):
            for y in range(self.n_col):
                if matrix[x][y] == 0:
                    visited.add(self.n_col * x + y)
                    queue.append([x, y])
        while len(queue) > 0:
            node = queue.pop(0)
            node_x, node_y = node
            neighbours = self.get_next(node)
            for neighbour in neighbours:
                neighbour_x, neighbour_y = neighbour
                if self.n_col * neighbour_x + neighbour_y not in visited:
                    matrix[neighbour_x][neighbour_y] = matrix[node_x][node_y] + 1
                    queue.append(neighbour)
                    visited.add(self.n_col * neighbour_x + neighbour_y)
        return matrix

    def get_next(self, pos):

        x, y = pos
        next_positions = list(
            filter(
                lambda x: x[0] >= 0 and x[0] < self.n_row and x[1] >= 0 and x[1] < self.n_col,
                [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]],
            )
        )
        return next_positions
