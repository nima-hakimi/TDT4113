"""
Test
"""


from calculator import Calculator

calc_str = input("What do you want to calculate?: ")

calc = Calculator()

print(calc.calculate(calc_str))

