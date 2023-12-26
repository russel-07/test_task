# Для реализации очереди в данном классе используется массив.
# Элементы очереди хранятся в последовательных ячейках
# памяти, что ускоряет доступ к данным. Сложность добавления,
# извлечения и поиска элемента в данной реализации составляет O(1).
# Недостатком данной реализации является ограничение максимального размера
# очереди.

class ArrayQueue:

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


# Для реализации очереди в данном классе используется связный список.
# В данной реализации нет ограничения на максимальный размер очереди.
# Элементы очереди хранятся в произвольных ячейках памяти, что замедляет
# итерацию по элементам, а также требуется выделение дополнительной памяти
# для хранения указателей.
# Сложность операций добавления и извлечения элемента из очереди составляет
# O(1), сложность поиска элемента в очереди в худшем случае составляет O(n).

class LinkedListQueue:

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


def check_ArrayQueue_class():
    queue = ArrayQueue(5)
    assert queue.buffer == [None] * 5
    assert queue.get() == 'Buffer is empty'
    assert queue.put(1) == None
    assert queue.put(2) == None
    assert queue.put(3) == None
    assert queue.put(4) == None
    assert queue.put(5) == None
    assert queue.buffer == [1, 2, 3, 4, 5]
    assert queue.put(6) == 'Buffer is full'
    assert queue.get() == 1
    assert queue.get() == 2
    assert queue.get() == 3
    assert queue.get() == 4
    assert queue.get() == 5
    assert queue.get() == 'Buffer is empty'
    print('ArrayQueue class works correctly!')


def check_LinkedListQueue_class():
    queue = LinkedListQueue()
    assert queue.get() == 'Buffer is empty'
    assert queue.put(1) == None
    assert queue.put(2) == None
    assert queue.put(3) == None
    assert queue.put(4) == None
    assert queue.put(5) == None
    assert queue.get() == 1
    assert queue.get() == 2
    assert queue.get() == 3
    assert queue.get() == 4
    assert queue.get() == 5
    assert queue.get() == 'Buffer is empty'
    print('LinkedListQueue class works correctly!')
