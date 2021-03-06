class Solution:
    '''brute force'''
    def trap(self, height: List[int]) -> int:
        left = 0
        right= len(height)-1
        answer = 0
        for idx,wall in enumerate(height):
            left_max = max(height[:idx+1])
            right_max = max(height[idx:])
            min_wall = min(left_max,right_max)
            answer += max(min_wall-wall,0)
        return answer


class Solution:
    '''two pointer solution'''
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_max= 0
        right_max = len(height)-1
        answer = 0
        
        while left<=right:
            if height[left_max]>height[right_max]:
                if height[right_max]<height[right]:
                    right_max=right
                answer += height[right_max]-height[right]
                right-=1
            else:
                if height[left_max]<height[left]:
                    left_max=left
                answer += height[left_max]-height[left]
                left+=1    
        return answer
                