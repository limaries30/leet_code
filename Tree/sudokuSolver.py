class Solution:
    def solveSudoku(self, board):

        """
        Do not return anything, modify board in-place instead.
        """

        self.row = len(board)
        self.col = len(board[0])
        self.row_start = 0

        self.board = board

        for i in range(self.row_start, self.row):
            for j in range(self.col):
                if self.board[i][j] == ".":
                    for k in range(1, 10):
                        self.board[i][j] = str(k)
                        if not self.isValidSudoku(self.board):
                            self.board[i][j] = "."
                        else:
                            self.row_start = i
                            if self.solveSudoku(self.board):
                                return True
                            else:
                                self.board[i][j] = "."
                    return False
        return True

    def isValidSudoku(self, board) -> bool:
        row = len(board)
        col = len(board[0])

        row_map = [set() for i in range(9)]
        col_map = [set() for j in range(9)]
        k_map = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                r = row_map[i]
                c = col_map[j]
                k = k_map[i // 3 + 3 * (j // 3)]

                tmp = board[i][j]

                if tmp != ".":
                    tmp = int(tmp)
                    if tmp in r or tmp in c or tmp in k:
                        return False
                    r.add(tmp)
                    c.add(tmp)
                    k.add(tmp)
        return True


a = Solution()
sudoku = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."],
]
print(sudoku)
a.solveSudoku(sudoku)
print(sudoku)