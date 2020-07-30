class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        queue = []
        result=[]
        
        for i in s:
            if i==')':
                while queue:
                    tmp = queue.pop(0)
                    if tmp=='(':
                        result.append(tmp)
                        queue.append(i)
                        break
                    result.append(tmp)
            else:
                queue.append(i)
        for i in queue:
            if i!='(':
                result.append(i)
                
        return ''.join(result)