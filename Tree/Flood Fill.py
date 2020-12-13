class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        self.rows = len(image)
        self.cols = len(image[0])
        self.visited = set()

        original_color = image[sr][sc]
        
        q = deque()
        q.append([sr,sc])
        
        while len(q)>0:
            item = q.popleft()
            x,y = item
            
            if image[x][y]==original_color:
                image[x][y]=newColor
                self.visited.add((x,y))
                neighbor = self.get_neighbor(x,y)
                q.extend(neighbor)

        return image
        
    
    def get_neighbor(self,sr,sc):
        
        coordinates = [[sr+1,sc],[sr,sc+1],[sr,sc-1],[sr-1,sc]]
        coordinates = list(filter(lambda x:x[0]>=0 and x[0]<self.rows and x[1]>=0 and x[1]<self.cols,coordinates))
        coordinates = list(filter(lambda x:(x[0],x[1]) not in self.visited,coordinates))
        
        return coordinates
        