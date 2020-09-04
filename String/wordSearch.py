'''
https://leetcode.com/problems/word-search/
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''
class Solution:
    
    def exist(self, board, word) -> bool:

        
        self.row = len(board)
        self.col = len(board[0])
        self.board = board
        self.word = word
        start = word[0]
        result = False
        
        for r_idx,row_data in enumerate(board):
            if start in row_data:
                idx_list = [i for i,ele in enumerate(row_data) if ele==start]
                for idx in idx_list:
                    self.board[r_idx][idx] = 0
                    result = self.Find([r_idx,idx],1)
                    self.board[r_idx][idx] = start
                    if result:
                        return result
        return result
                
        
    
    def move(self,idx):
        
        x,y =idx
        neib = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        movs = list(filter(lambda x:((x[0]>=0 and x[1]>=0) and (x[0]<self.row and x[1]<self.col)),neib))
        
        return movs
    
    def Find(self,pos,idx):
        
        if idx==len(self.word):
            return True
        
        result = False
        pos_neibs = self.move(pos)
        for neib in pos_neibs:
            
            x,y=neib
            if not self.board[x][y]:
                continue
            if self.board[x][y]==self.word[idx]:
                self.board[x][y] = 0
                result = self.Find([x,y],idx+1)
                self.board[x][y] = self.word[idx]
        
            if result:
                return result
            
        return result
