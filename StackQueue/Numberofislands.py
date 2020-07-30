class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        self.width = len(grid[0])
        self.height=len(grid)
        self.grid = grid
        self.cnt = 0
        self.ch = [[0 for i in range(self.width)] for j in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j]=='1' and not self.ch[i][j]:
                    self.cnt+=1
                    self.setDFS((i,j))
        return self.cnt
        
            
    def RetrurnNeighbour(self,idx):
        x,y = idx
        neighs = [(x,y+1),(x+1,y),(x-1,y),(x,y-1)]
        clipped_neighs = list(filter(lambda x:x[0]>=0 and x[1]>=0 and x[0]<self.height and x[1]<self.width,neighs))
        return clipped_neighs
    
    def setDFS(self,idx):
        x,y = idx
        self.ch[x][y] = self.cnt
        neighbors = self.RetrurnNeighbour(idx)
        for i in neighbors:
            i_x,i_y = i
            if self.grid[i_x][i_y]=='1' and not self.ch[i_x][i_y]:
                self.setDFS(i)
                