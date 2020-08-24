'''
https://leetcode.com/problems/valid-sudoku/
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''
class Solution:
    '''using set'''
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
                k = k_map[i//3+3*(j//3)]
                
                tmp = board[i][j]
                
                if tmp!='.':
                    tmp = int(tmp)
                    if tmp in r or tmp in c or tmp in k:
                        return False
                    r.add(tmp)
                    c.add(tmp)
                    k.add(tmp)
        return True


class Solution:
    '''brute force'''
    def isValidSudoku(self, board) -> bool:
        row = len(board)
        self.board = board

        for i in range(row):
        
            col = len(board[i])
            ch = [0 for i in range(col)]
            for j in range(col):
                item = board[i][j]
                if item!='.' and ch[int(item)-1]:
                    return False
                if item!='.':
                    ch[int(item)-1]=1
        
        for j in range(col):
            row = len(board)
            ch = [0 for i in range(row)]
            for i in range(row):
                item = board[i][j]
                if item!='.' and ch[int(item)-1]:
                    return False
                if item!='.':
                    ch[int(item)-1]=1     
            
        mids = [[i,j] for j in [0,3,6] for i in [0,3,6]]
        
        for mid in mids:
            if not self.isValid(mid):
                return False
        return True

    def isValid(self,mid):
        x=mid[0]
        y=mid[1]
        ch = [0 for i in range(9)]
        for i in range(3):
            for j in range(3):
                item = self.board[x+i][y+j]
                if item!='.' and ch[int(item)-1]:
                        return False
                if item!='.':
                    ch[int(item)-1]=1   
        return True
        

test = [[".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]]

ans = Solution().isValidSudoku(test)
print('ans',ans)