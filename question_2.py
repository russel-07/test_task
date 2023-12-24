class ArrayRingBuffer:

    def __init__(self, size):
        self.size = size
        self.first = 0
        self.last = 0
        self.count = 0
        self.buffer = [None for _ in range(size)]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def add(self, value):
        if self.is_full():
            return 'Buffer is full'
        else:
            self.buffer[self.last] = value
            self.count += 1
            self.last = (self.last + 1) % self.size

    def push(self):
        if self.is_empty():
            return 'Buffer is empty'
        else:
            value = self.buffer[self.first]
            self.buffer[self.first] = None
            self.count -= 1
            self.first = (self.first + 1) % self.size
            return value

        
class LinkedListRingBuffer:

    class Node:

        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, value):
        if self.is_empty():
            self.head = self.Node(value)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value)
            self.tail = self.tail.next

    def push(self):
        if self.is_empty():
            return 'Buffer is empty'
        else:
            value = self.head.value
            self.head = self.head.next
            return value

