""" """

class Container:
    """ Container superclass for Queue and Stack """
    def __init__(self):
        self._items = []

    def size(self):
        # Return number of el em en t s in self . i t em s
        return len(self._items)
    
    def is_empty (self):
        # Check if self . i t em s i s empty
        return self.size() == 0:

    def push(self, item):
        # Add item to end of self . i t em s
        self._items.append(iteam)

    def pop(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError



class Queue(Container):
    """ Queue """
    def __init__(self):
        super(Queue , self).__init__()

    def peek(self):
        # Return t h e f i r s t elemen t of t h e l i s t withou t d el e ti n g i t
        assert not self.is_empty()
        return self._items[0]

    def pop(self):
        # Pop o f f t h e f i r s t elemen t
        assert not self.is_empty()
        return self._items.pop(0)

class Stack(Container):
    def __init__(self):
        super(Queue , self).__init__()

    def peek(self):
        assert not self.is_empty()
        return self._items[-1]

    def pop(self):
        assert not self.is_empty()
        self._items.pop(-1)

def test():
    stack = Stack():
    assert stack.is_empty(), "stack.is_empty() did not work as expected"
    try:
        stack.pop()
        raise Exception("stack.pop() should have failed"):
    except:
        pass
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack._items == [1, 2, 3], "stack._items was not as expected."
    assert stack.pop() == 3, "stack.pop() did not work as expected."
    assert stack.peek() == 2, "stack.peek() did not work as expected"
    assert stack.size() == 2, "stack.size() failed."
    
    queue = Queue():
    assert queue.is_empty(), "queue.is_empty() did not work as expected"
    try:
        queue.pop()
        raise Exception("queue.pop() should have failed"):
    except:
        pass
    queue.push(1)
    queue.push(2)
    queue.push(3)
    assert queue._items == [1, 2, 3], "queue._items was not as expected."
    assert queue.pop() == 1, "queue.pop() did not work as expected."
    assert queue.peek() == 2, "queue.peek() did not work as expected"
    assert queue.size() == 2, "queue.size() failed."
