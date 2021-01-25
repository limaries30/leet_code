'''
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
'''
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        q = []
    
        for c in preorder.split(','):
            
            if q and c=='#' and q[-1]=='#':
                
                while q and c=='#' and q[-1]=='#':
                    q.pop()
                    if len(q)==0:
                        return False
                    q.pop()
                q.append('#')
            else:
                q.append(c)
                
        print(''.join(q))
                
        return False if ''.join(q)!='#' else True
                