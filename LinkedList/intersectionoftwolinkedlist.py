
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
            '''방문체크,None이면 그대로 return'''
            if head is not None:
                head.visited = True
                head = head.next
            return head

                