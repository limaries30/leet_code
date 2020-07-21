
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        ans = ListNode(val=0)  #dummynode
        current_ans = ans
        prev=0

        while l1 or l2:

            l1_val,l1 =[l1.val,l1.next] if l1 is not None else [0,None]
            l2_val,l2 = [l2.val,l2.next] if l2 is not None else [0,None]
            num = l1_val + l2_val+prev    
            
            prev,num = divmod(num,10)
            current_ans.next =ListNode(val=num)
            current_ans = current_ans.next
 
        #마지막 더한 숫자가 10을 넘어간다면
        if prev>0:
            current_ans.next = ListNode(prev)
                
        return ans.next



'''Testing'''
def GenerateLinks(x):
    link = ListNode(x[0],next=None)
    current_link = link
    for i in x[1:]:
        current_link.next = ListNode(i,next=None)
        current_link = current_link.next
        
    return link

a = GenerateLinks([2,4,3])
b= GenerateLinks([5,6,4])

Solution().addTwoNumbers(a,b)
