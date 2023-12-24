from question_1 import isEven
from question_2 import ArrayRingBuffer, LinkedListRingBuffer

a = ArrayRingBuffer(5)
b = LinkedListRingBuffer

if __name__ == '__main__':
    assert isEven(0) == True
    assert isEven(1) == False
    assert isEven(12) == True
    assert isEven(12345) == False
    assert a.push() == 'Buffer is empty'