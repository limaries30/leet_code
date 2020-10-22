'''
7. Reverse Integer
Easy

3852

5999

Add to List

Share
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 
'''
class Solution:
    def reverse(self, x: int) -> int:
        str_x=str(x)
        
        if '-' not in str_x:
            return self.make(str_x)
        else:
            return -self.make(str_x[1:])
        
    def make(self,x:str,):
        
        return self.rectify(int(''.join(list(x)[::-1])))
    
    def rectify(self,x):
        if x>pow(2,31)-1 or x<-pow(2,31):
            return 0
        else:
            return x