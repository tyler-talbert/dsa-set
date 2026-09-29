class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity_limit = k
        self.capacity = 0
        self.dummy = Node(-1)
        
    def enQueue(self, value: int) -> bool:
        if self.capacity == self.capacity_limit:
            return False

        curr = Node(value)
        if self.capacity == 0:
            # There are currently no nodes, head & tail is this new node
            self.dummy.nxt = self.dummy.prev = curr
            curr.nxt = curr.prev = self.dummy
        else:
            cur_tail = self.dummy.nxt
            cur_tail.prev = curr
            curr.nxt = cur_tail
            curr.prev = self.dummy
            self.dummy.nxt = curr

        self.capacity += 1

        return True

    def deQueue(self) -> bool:
        if not self.capacity:
            return False

        removal_node = self.dummy.prev
        next_up = removal_node.prev
        next_up.nxt = self.dummy
        self.dummy.prev = next_up

        self.capacity -= 1
        return True

    def Front(self) -> int:
        return self.dummy.prev.val if self.capacity > 0 else -1
        

    def Rear(self) -> int:
        return self.dummy.nxt.val if self.capacity > 0 else -1
        

    def isEmpty(self) -> bool:
        return self.capacity == 0

    def isFull(self) -> bool:
        return self.capacity == self.capacity_limit
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()