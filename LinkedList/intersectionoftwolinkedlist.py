
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
 
        if headA == headB:
            return headA
        
        while True:
            
            nextA = self.UpdateNode(headA)
            nextB = self.UpdateNode(headB)
       
            #종료 조건 check하고 다음 노드로 넘어가기
            if nextA == nextB:
                return nextB    
            elif hasattr(nextA,'visited'):
                return nextA
            elif hasattr(nextB,'visited'):
                return nextB
            elif nextA is None and nextB is None:
                return None            
            else:
                headA = nextA
                headB = nextB
                
    def UpdateNode(self,head:ListNode)->ListNode:
        
        if head is not None:
            nextNode = head.next
            head.visited = True
        else:
            nextNode = None
            
        return nextNode
                