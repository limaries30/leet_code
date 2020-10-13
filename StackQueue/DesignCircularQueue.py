'''
622. Design Circular Queue
Medium

672

91

Add to List

Share
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
'''
class MyCircularQueue:

def __init__(self, k: int):
    """
    Initialize your data structure here. Set the size of the queue to be k.
    """
    
    self.head = 0
    self.tail = 0
    self.k = k
    self.q = [False for i in range(k)]

def get_next_idx(self,idx):
    if idx+1>self.k-1:
        return 0
    else:
        return idx+1

def enQueue(self, value: int) -> bool:
    """
    Insert an element into the circular queue. Return true if the operation is successful.
    """
    next_idx = self.get_next_idx(self.tail)
    if self.q[self.tail] is False:
        self.q[self.tail] = value
        self.tail = self.get_next_idx(self.tail)
        return True
    else:
        return False

def deQueue(self) -> bool:
    """
    Delete an element from the circular queue. Return true if the operation is successful.
    """
    if self.q[self.head] is not False:
        self.q[self.head] = False
        self.head = self.get_next_idx(self.head)
        return True
    else:
        return False
    

def Front(self) -> int:
    """
    Get the front item from the queue.
    """
    if self.isEmpty():
        return -1
    else:
        return self.q[self.head]
    

def Rear(self) -> int:
    """
    Get the last item from the queue.
    """
    if self.isEmpty():
        return -1
    else:
        return self.q[self.tail-1]

def isEmpty(self) -> bool:
    """
    Checks whether the circular queue is empty or not.
    """
    return True if self.q[self.head] is False else False

def isFull(self) -> bool:
    """
    Checks whether the circular queue is full or not.
    """
    return True if self.head==self.tail and self.q[self.head] else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()