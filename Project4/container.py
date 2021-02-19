""" """

class Container:
    """ Container superclass for Queue and Stack """
    def __init__(self):
        self. items = []

    def size(self):
        # Return number of el em en t s in self . i t em s
    
    def is_empty (self):
        # Check i f self . i t em s i s empty

    def push(self, item):
        # Add item to end of self . i t em s

    def pop(self):
        # Pop o f f t h e c o r r e c t elemen t of self . i tems , and re turn i t
        # This method d i f f e r s between s ub cl a s s e s , hence i s not
        # implemented in t h e s u p e r cl a s s
        raise NotImplementedError

    def peek(self):
        # Return t h e top elemen t wi thou t removing i t
        # This method d i f f e r s between s ub cl a s s e s , hence i s not
        # implemented in t h e s u p e r cl a s s
        raise NotImplementedError



class Queue(Container):
    """ Queue """
    def __init__(self):
        super(Queue , self).__init__()

    def peek(self):
        # Return t h e f i r s t elemen t of t h e l i s t withou t d el e ti n g i t
        assert not self.is_empty ()
        return self.items[0]

    def pop(self):
        # Pop o f f t h e f i r s t elemen t
        assert not self.is_empty()
        return self. items .pop (0)

class Stack(Container):
    def __init__(self):
        super(Queue , self).__init__()

