""" Defining the Stack and Queue classes, as well as unit test for both """


class Container:
    """ Container superclass for Queue and Stack """
    def __init__(self):
        self._items = []

    def get_items(self):
        """ Returns items-list """
        return self._items

    def size(self):
        """ Returns items-list size """
        return len(self._items)

    def is_empty(self):
        """ Returns true if the list is empty, otherwise false """
        return self.size() == 0

    def push(self, item):
        """ Adds the input to the end of items-list """
        self._items.append(item)

    def pop(self):
        """ Method for removing element according to the sub-class """
        raise NotImplementedError

    def peek(self):
        """ Peeks the next element in the item-list """
        raise NotImplementedError


class Queue(Container):
    """ Queue """
    def peek(self):
        assert not self.is_empty()
        return self._items[0]

    def pop(self):
        assert not self.is_empty()
        return self._items.pop(0)


class Stack(Container):
    """ Stack """
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
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.get_items() == [1, 2, 3], "stack._items was not as expected."
    assert stack.pop() == 3, "stack.pop() did not work as expected."
    assert stack.peek() == 2, "stack.peek() did not work as expected"
    assert stack.size() == 2, "stack.size() failed."

    # Queue
    queue = Queue()
    assert queue.is_empty(), "queue.is_empty() did not work as expected"
    queue.push(1)
    queue.push(2)
    queue.push(3)
    assert queue.get_items() == [1, 2, 3], "queue._items was not as expected."
    assert queue.pop() == 1, "queue.pop() did not work as expected."
    assert queue.peek() == 2, "queue.peek() did not work as expected"
    assert queue.size() == 2, "queue.size() failed."

    print('Stack and Queue works as expected')


if __name__ == "__main__":
    test()
