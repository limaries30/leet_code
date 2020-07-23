from utils import GenerateLinks,ListNode


class MySolution:
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

class FastestSolution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2:
            new = carry
            if l1:
                new += l1.val
                l1 = l1.next
            if l2:
                new += l2.val
                l2 = l2.next
            carry = new // 10
            cur.next = ListNode(new % 10)
            cur = cur.next
        if carry > 0:
            cur.next = ListNode(carry)
        return dummy.next



a = GenerateLinks([2,4,3])
b= GenerateLinks([5,6,4])

MySolution().addTwoNumbers(a,b)
