class Container:
    def __init__(self):
        self._items = []

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return

    #def peek(self):

class Queue(Container):
    def __init__(self):
        super(Queue, self).__init__()

    def peek(self): #Sjekke hvilket element som vil bli poppet
        if self.is_empty():
            print("kan ikke peeke en tom kø")
            return
        return self._items[0]

    def pop(self):
        if self.is_empty():
            print("kan ikke poppe en tom kø")
            return
        return self._items.pop(0)

class Stack(Container):
    def __init__(self):
        super(Stack, self).__init__()

    def peek(self): #Sjekke hvilket element som vil bli poppet
        if self.is_empty():
            print("kan ikke peeke en tom stack")
            return
        return self._items[-1]

    def pop(self):
        if self.is_empty():
            print("kan ikke poppe en tom stack")
            return
        return self._items.pop(-1)


#Det fungerer!
"""test = Stack()
test.push(1)
test.push(2)
print(test.pop())
print(test.size())"""













