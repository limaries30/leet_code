class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [0,1]
        position = [0,0]
        
        for i in range(4):
            for instruction in instructions:
                if instruction=='G':
                    position = self.row_add(position,direction)
                if instruction=='R':
                    direction = self.turnRight(direction)
                if instruction=='L':
                    direction = self.turnLeft(direction)
        
        return True if position[0]==0 and position[1]==0 else False
        
        
    def row_add(self,x,y):
        
        for i in range(len(x)):
            x[i]+=y[i]
        
        return x
        
    def row_multiplication(self,row,matrix):
        '''row*matrix'''
        rotated_vector = [0,0]
        
        for idx,row_vector in enumerate(matrix):
            scale = row[idx]
            scaled_row_vecotr = [ele*scale for ele in row_vector]
            rotated_vector = self.row_add(scaled_row_vecotr,rotated_vector)
        
        return rotated_vector
          
    def turnRight(self,x):
        
        right_rotation_matrix = [[0,-1],[1,0]]
        rotated_position = self.row_multiplication(x,right_rotation_matrix)
        
        return rotated_position
            
    def turnLeft(self,x):
        
        left_rotation_matrix = [[0,1],[-1,0]]
        rotated_position = self.row_multiplication(x,left_rotation_matrix)
        
        return rotated_position
        
        