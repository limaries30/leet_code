'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

https://leetcode.com/problems/merge-k-sorted-lists/submissions/'''

from queue import PriorityQueue

class Solution:
    '''우선순위큐를 이용'''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        q= PriorityQueue()
        answer = ListNode()
        answer_head = answer

        for idx,i in enumerate(lists):
            if i:
                q.put((i.val,idx))

        while not q.empty():
            tmp = q.get()
            val = tmp[0]
            idx = tmp[1]
            
            answer.next = ListNode(val)
            answer = answer.next
            
            lists[idx] = lists[idx].next
            if lists[idx]:
                q.put((lists[idx].val,idx))
                
        return answer_head.next
            