import numbers
import numpy
import re
from container import Stack, Queue
from Function import Function, Operator
from calculator import Calculator

"""
rekkefølge:
- calc = Calculator()
- text = "regnestykke", EXP(1 GANGE (3 PLUSS 4)) : 
- text_p
"""

def test(prompt):
    calc = Calculator()
    text = prompt
    parsedText = calc.text_parser(text)
    #for i in parsedText:
    #    print(i)
    calc.outputQueueMaker(parsedText)  # changes self.outputqueue directly
    result = calc.calculate()
    print(text + " = " + str(result))

text = input("Hva vil du regne ut?  ")
text1 = "SQRT(27 DELE (5 MINUS 2))"
text2 = "COS(2 GANGE EXP(2))"
text3 = "EXP(4 GANGE (3 PLUSS 4) DELE (5 MINUS 1))"

test(text)