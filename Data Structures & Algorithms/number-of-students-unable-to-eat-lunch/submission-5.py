class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def __init__(self):
        self.left = None
        self.right = None

    def enqueue(self, val):
        new_node = Node(val)

        if self.right:
            self.right.next = new_node
            self.right = self.right.next
        else:
            self.right = self.left = new_node
        return new_node
    
    def dequeue(self):
        if not self.left:
            return None

        val = self.left.val
        if self.left.next:
            self.left = self.left.next
        else:
            self.left = None
        return val

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for val in students:
            self.enqueue(val)

        count = 0
        while count <= len(students):
            if self.left and self.left.val == sandwiches[0]:
                sandwiches.pop(0)
                self.dequeue()
                count = 0
            else:
                student = self.dequeue()
                self.enqueue(student)
                count += 1
            if len(sandwiches) == 0:
                return 0
        
        result = 0
        if not self.left:
            return 1
        while self.left.next:
            self.left = self.left.next
            result += 1
        return result + 1
