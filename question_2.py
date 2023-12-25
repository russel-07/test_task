class ArrayRingBuffer:

    def __init__(self, size):
        self.buffer = [None for _ in range(size)]
        self.max_size = size
        self.head = 0
        self.tail = 0
        self.current_size = 0

    def is_empty(self):
        return self.current_size == 0

    def is_full(self):
        return self.current_size == self.max_size

    def put(self, value):
        if self.is_full():
            return 'Buffer is full'
            # raise ValueError('Buffer is full')
        self.buffer[self.tail] = value
        self.current_size += 1
        self.tail = (self.tail + 1) % self.max_size

    def get(self):
        if self.is_empty():
            return 'Buffer is empty'
            # raise ValueError('Buffer is empty')
        value = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.current_size -= 1
        return value

        
class LinkedListRingBuffer:

    class Node:

        def __init__(self, value, next=None):
            self.value = value
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def put(self, value):
        if self.is_empty():
            self.head = self.Node(value)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value)
            self.tail = self.tail.next

    def get(self):
        if self.is_empty():
            return 'Buffer is empty'
            # raise ValueError('Buffer is empty')
        value = self.head.value
        self.head = self.head.next
        return value
