""" Calculator class """


import numbers
import numpy
import re
from container import Stack, Queue
from function import Function, Operator

class Calculator:
    def __init__(self):
        self.functions = {'EXP': Function(numpy.exp),
                          'LOG': Function(numpy.log),
                          'SIN': Function(numpy.sin),
                          'COS': Function(numpy.cos),
                          'SQRT': Function(numpy.sqrt)}

        self.operators = {'ADD': Operator(numpy.add, 0),
                          'PLUS': Operator(numpy.add, 0),
                          'MULTIPLY': Operator(numpy.multiply, 1),
                          'DIVIDE': Operator(numpy.divide, 1),
                          'SUBTRACT': Operator(numpy.subtract, 0),
                          'MINUS': Operator(numpy.subtract, 0)}

        self.output_queue = Queue()

    def evaluate(self):
        """
        ...
        """
        pass

    def convert_queue_to_rpn(self):
        """
        ...
        """
        pass

    def text_parser(self):
        """
        ...
        """
        pass

    def calculate(self):
        """
        Put everything together
        """
        pass


def test():
    calc = Calculator ()
    print(calc.functions['EXP'].execute(
          calc.operators['ADD'].execute (1,
          calc.operators['MULTIPLY'].execute (2, 3))))

if __name__ == '__main__':
    test()