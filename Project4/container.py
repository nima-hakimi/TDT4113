""" """

class Container:
    """ Container superclass for Queue and Stack """
    def __init__(self):
        self._items = []

    def size(self):
        return len(self._items)
    
    def is_empty (self):
        return self.size() == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return

    def peek(self):
        raise NotImplementedError



class Queue(Container):
    """ Queue """
    def __init__(self):
        super(Queue , self).__init__()

    def peek(self):
        assert not self.is_empty()
        return self._items[0]

    def pop(self):
        assert not self.is_empty()
        return self._items.pop(0)

class Stack(Container):
    def peek(self):
        assert not self.is_empty()
        return self._items[-1]

    def pop(self):
        assert not self.is_empty()
        return self._items.pop(-1)

def test():
    """ Units tests for Stack and Queue """

    # Stack
    stack = Stack()
    assert stack.is_empty(), "stack.is_empty() did not work as expected"
    assert stack._items == [1, 2, 3], "stack._items was not as expected."
    assert stack.pop() == 3, "stack.pop() did not work as expected."
    assert stack.peek() == 2, "stack.peek() did not work as expected"
    assert stack.size() == 2, "stack.size() failed."
    
    # Queue
    queue = Queue()
    assert queue.is_empty(), "queue.is_empty() did not work as expected"
    queue.push(1)
    queue.push(2)
    queue.push(3)
    assert queue._items == [1, 2, 3], "queue._items was not as expected."
    assert queue.pop() == 1, "queue.pop() did not work as expected."
    assert queue.peek() == 2, "queue.peek() did not work as expected"
    assert queue.size() == 2, "queue.size() failed."
