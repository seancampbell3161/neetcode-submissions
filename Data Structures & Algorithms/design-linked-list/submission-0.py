class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, None, None)
            self.tail = self.head
        else:
            new_head = Node(val, self.head, None)
            self.head.prev = new_head
            self.head = new_head

        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        new_tail = Node(val, None, self.tail or None)
        self.tail.next = new_tail
        self.tail = new_tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            new_node = Node(val, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node
        elif index > self.size - 1:
            return
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next

            new_node = Node(val, curr, curr.prev)
            curr.prev.next = new_node
            curr.prev = new_node

        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.head: self.head.prev = None
            else: self.tail = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail: self.tail.next = None
            else: self.head = None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)