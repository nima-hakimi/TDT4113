import numbers
import numpy

class Operator:
    def __init__(self, operation, strength):
        self.operation = operation
        self.strength = strength

    def getStrength(self):
        return self.strength

    def execute(self, n1, n2):
        if not (isinstance(n1, numbers.Number) and isinstance(n2, numbers.Number)): # Sjekker om element er tall (int eller float)
            raise TypeError("Cannot execute func if element is not a number")
        result = self.operation(n1, n2)
        return result

class Function:
    def __init__(self, func):
        self.func = func

    def execute(self, element):
        if not isinstance(element, numbers.Number): # Sjekker om element er tall (int eller float)
            raise TypeError("Cannot execute func if element is not a number")
        result = self.func(element)
        return result
    # nå kan vi opprette f.eks:

"""exponential_func = Function(numpy.exp)
sin_func = Function(numpy.sin)
print(exponential_func.execute(sin_func.execute(0)))
print(isinstance(exponential_func, Function))"""

"""add_op = Operator(numpy.add, 0)
multiply_op = Operator(numpy.multiply, 1)
print(add_op.execute(1, multiply_op.execute(2, 3)))"""

