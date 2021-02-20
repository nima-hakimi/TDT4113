"""
Function and Operator class
- operator.py is unavailable
"""


import numbers
import numpy

class Function:
    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=False:
        if not isinstance(element, numbers.Number):
            raise TypeError('The element must be a number')
        result = self.func(element)

        if debug:
            print('Function: ' + self.func.__name__
                    + "(%s) = %s" % (element , result))

        return result

class Operator:
    def __init__(self, operation, strength):
        self.operation = operation
        self.strength = strength

    def get_strength(self):
        return self.strength

    def execute(self, n1, n2):
        if not (isinstance(n1, numbers.Number) and isinstance(n2, numbers.Number)):
            raise TypeError('The element must be a number')
        result = self.operation(n1, n2)
        return result

def test():
    """ Tests for Function and Operator """

    print('TEST FUNCTION:')
    exponential_func = Function(numpy.exp)
    sin_func = Function(numpy.sin)
    print(exponential_func.execute(sin_func.execute(0)))
    print(isinstance(exponential_func, Function))

    print('\nTEST OPERATOR:')
    add_op = Operator(numpy.add, 0)
    multiply_op = Operator(numpy.multiply, 1)
    print(add_op.execute(1, multiply_op.execute(2, 3)))

if __name__ == '__main__':
    test()
