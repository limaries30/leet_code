"""
https://leetcode.com/problems/copy-list-with-random-pointer/

'A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        NewNode = self.deepcopy(head)
        
        return NewNode
    
    def deepcopy(self,x):
        
        if not hasattr(x,'cloned'):
            NewNode = Node(x=x.val)
            x.cloned = NewNode
            if x.next is not None:
                if not hasattr(x.next,'cloned'):
                    NewNode.next = self.deepcopy(x.next)
                else:
                    NewNode.next = x.next.cloned
            if x.random is not None:
                if not hasattr(x.random,'cloned'):
                    NewNode.random = self.deepcopy(x.random)
                else:
                    NewNode.random = x.random.cloned

        return x.cloned



class Solution:
    '''O(N)/O(1)'''
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        StartHead = head
        
        if head is None:
            return None
        
        #복제하기
        while head is not None:
            NextHead = Node(x=head.val)
            original_next = head.next
            NextHead.next = original_next
            head.next = NextHead
            head = original_next
        
        #Random pointer 변경
        RandomStartHead = StartHead
        while RandomStartHead is not None:
            if RandomStartHead.random is not None:
                RandomStartHead.next.random = RandomStartHead.random.next
            else:
                RandomStartHead.next.random = None
            RandomStartHead = RandomStartHead.next.next
            
        #Nextpointer 변경
        ClonedStartHead = StartHead.next
        while ClonedStartHead is not None:
            if ClonedStartHead.next is not None:
                ClonedStartHead.next = ClonedStartHead.next.next
            else:
                ClonedStartHead.next = None
            ClonedStartHead = ClonedStartHead.next
        return StartHead.next