class ArrayFifoRingBuffer:

    def __init__(self, size):
        self.buffer_size = size
        self.first_index = 0
        self.last_index = 0
        self.val_counter = 0
        self.buffer = [None for _ in range(size)]

    def buffer_is_empty(self):
        return self.val_counter == 0
    
    def buffer_is_full(self):
        return self.val_counter == self.buffer_size

    def index_is_last(self, index):
        return index == self.buffer_size - 1
    
    def add(self, value):
        if self.buffer_is_full():
            return 'Buffer is full'
        else:
            self.buffer[self.last_index] = value
            self.val_counter += 1
            if self.index_is_last(self.last_index):
                self.last_index = 0
            else:
                self.last_index += 1
            return f'Added new value {value}'

    def push(self):
        if self.buffer_is_empty():
            return 'Buffer is empty'
        else:
            value = self.buffer[self.first_index]
            self.buffer[self.first_index] = None
            self.val_counter -= 1
            if self.index_is_last(self.first_index):
                self.first_index = 0
            else:
                self.first_index += 1
            return f'Push value {value}'

        
class LinkedListFifoRingBuffer:
    pass
