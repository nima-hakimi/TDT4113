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
        self.input_queue = Queue()

    def evaluate(self):
        """
        ...
        """
        stack = Stack()
        for i in range(self.output_queue.size()):
            element = self.output_queue.pop()
            if isinstance(element, numbers.Number):
                stack.push(element)
            elif isinstance(element, Function):
                num = stack.pop()
                calculated_value = element.execute(num)
                stack.push(calculated_value)
            elif isinstance(element, Operator):
                num1 = stack.pop()
                num2 = stack.pop()
                calculated_value = element.execute(num1, num2)
                stack.push(calculated_value)
            else:
                raise Exception("Wrong type in the output_queue")

        if stack.size() != 1:
            raise Exception("Stack should be of size 1.")

        return stack.pop()

    def convert_queue_to_rpn(self):
        """
        ...
        """
        operator_stack = Stack()
        for i in range(self.input_queue.size()):
            element = self.input_queue.pop()
            if isinstance(element, numbers.Number):
                self.output_queue.push(element)
            elif isinstance(element, Function):
                operator_stack.push(element)
            elif element == "(":
                operator_stack.push(element)
            elif element == ")":
                while operator_stack.peek() != "(":
                    self.output_queue.push(operator_stack.pop())
                operator_stack.pop()
            elif isinstance(element, Operator):
                while operator_stack.size() != 0:
                    next_element = operator_stack.peek()
                    if isinstance(next_element, Operator):
                        if next_element.strength < element.strength:
                            break
                    elif next_element == "(":
                        break
                    self.output_queue.push(operator_stack.pop())
                operator_stack.push(element)
            else:
                raise Exception("Wrong type in input queue")

        for i in range(self.output_queue.size()):
            self.output_queue.push(operator_stack.pop())

    def text_parser(self):
        """
        ...
        """


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