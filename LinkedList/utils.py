class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def GenerateLinks(x:list)->ListNode:
    link = ListNode(x[0],next=None)
    current_link = link
    for i in x[1:]:
        current_link.next = ListNode(i,next=None)
        current_link = current_link.next
        
    return link