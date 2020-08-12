'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''


class Solution:
    def kthSmallest(self, matrix,k: int) -> int:
        row = len(matrix)
        cnt = 0
        
        while True:
            min_value = matrix[0][0]
            for i in range(row):
                
                if matrix[i][0]<=min_value:
                    min_idx = i
                    min_value = matrix[i][0]
            
            tmp = matrix[min_idx].pop(0)
            
            if len(matrix[min_idx])==0:
                matrix.pop(min_idx)
                row-=1
            
            cnt+=1
            if cnt==k:
                return tmp


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

k = 8

sol = Solution()
print(sol.kthSmallest(matrix,k))