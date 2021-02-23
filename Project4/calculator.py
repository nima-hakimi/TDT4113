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
                          'TIMES': Operator(numpy.multiply, 1),
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
                calculated_value = element.execute(num2, num1)
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

        for i in range(operator_stack.size()):
            self.output_queue.push(operator_stack.pop())

    def text_parser(self, text):
        """
        parse text with regex
        """
        text = text.replace(" ", "").upper()

        # Make match strings for regex
        functions = "|".join(["^" + func for func in self.functions.keys()])
        operators = "|".join(["^" + func for func in self.operators.keys()])
        parenthesis = "^[()]"
        nums = "^[-1234567890]+"

        while text != "":
            check_num = re.search(nums, text)  # Check if number
            if check_num is not None:
                matched_num = check_num.__getitem__(0)
                self.input_queue.push(float(matched_num))
                text = text[len(matched_num)::]
                continue

            check_par = re.search(parenthesis, text)  # Check if parenthesis
            if check_par is not None:
                matched_par = check_par.__getitem__(0)
                self.input_queue.push(matched_par)
                text = text[1::]
                continue

            check_op = re.search(operators, text)  # Check if operator
            if check_op is not None:
                matched_op = check_op.__getitem__(0)
                self.input_queue.push(self.operators[matched_op])
                text = text[len(matched_op)::]
                continue

            check_func = re.search(functions, text)  # Check if function
            if check_func is not None:
                matched_func = check_func.__getitem__(0)
                self.input_queue.push(self.functions[matched_func])
                text = text[len(matched_func)::]
                continue

        return self.input_queue
    
    def calculate(self, input_str):
        """
        Put everything together
        """
        self.text_parser(input_str)
        self.convert_queue_to_rpn()
        return self.evaluate()


def test_basics():
    calc = Calculator()
    print(calc.functions['EXP'].execute(
          calc.operators['ADD'].execute(1,
          calc.operators['MULTIPLY'].execute(2, 3))))


def test_evaluate():
    calc = Calculator()
    calc.output_queue.push(10)
    calc.output_queue.push(5)
    calc.output_queue.push(calc.operators['MINUS'])
    print(calc.evaluate())


def test_convert_queue_to_rpn():
    calc = Calculator()
    calc.input_queue.push(10)
    calc.input_queue.push(calc.operators['MINUS'])
    calc.input_queue.push(5)
    calc.convert_queue_to_rpn()
    for i in range(calc.output_queue.size()):
        print(calc.output_queue.pop())


def test_text_parser():
    calc = Calculator()
    string = '1 PLUS 2 TIMES 2'
    calc.text_parser(string)
    for i in range(calc.input_queue.size()):
        print(calc.input_queue.pop())


if __name__ == '__main__':
    test_basics()
    test_evaluate()
    test_convert_queue_to_rpn()
    test_text_parser()
