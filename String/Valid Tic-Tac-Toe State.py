'''
https://leetcode.com/problems/valid-tic-tac-toe-state/
'''

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        num_x = 0
        num_o = 0
        
        num_xxx = 0
        num_ooo = 0
        
        for i,row in enumerate(board):
            num_x += row.count('X')
            num_o += row.count('O')
            col = ''.join([board[r][i] for r in range(len(board))])
            if 'XXX' == row:
                num_xxx+=1
            if 'XXX' == col:
                num_xxx+=1
            if 'OOO' == row:
                num_ooo+=1
            if 'OOO' == col:
                num_ooo+=1

            
        num_xxx += self.check_diagonal(board,'X')
        num_ooo += self.check_diagonal(board,'O')
            
        if num_x==num_o:
            return False if num_xxx>0 else True
        if num_x==num_o+1:
            return False if num_ooo>0 else True
        return False
            
    
    def check_diagonal(self,board,symbol):
        
        num_yx = 0
        num_y_x = 0
        cnt = 0
        board_len = len(board)
        for i in range(board_len):
            if board[i][i] == symbol:
                num_yx += 1
            if board[board_len-1-i][i]==symbol:
                num_y_x += 1
        
        if num_yx==3:
            cnt+=1
        if num_y_x==3:
            cnt+=1 
                
        return cnt