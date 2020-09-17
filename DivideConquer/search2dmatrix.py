class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        num_row = len(matrix)
        num_col = len(matrix[0])
        
        c =0
        r = num_row-1
        
        while c<num_col and r>=0:
            if target == matrix[r][c]:
                return True
            if target>matrix[r][c]:
                c+=1
            else:
                r-=1
        return False