"""
Test
"""


from calculator import Calculator

CALC_STR = input("What do you want to calculate?: ")

CALC = Calculator()

print(CALC.calculate(CALC_STR))
