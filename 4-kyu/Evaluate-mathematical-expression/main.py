# Evaluate mathematical expression

dct_operations = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b, "/": lambda a, b: a / b, }

import re

def indexes(expression: str):
    match = re.findall(r"(.+)", expression)
    return match

def is_parentheses(count_of_parentheses: int, line: str, lst: list):
    pass


def calc(expression: str) -> int:
    number = 0
    count_of_parentheses = expression.count("(")

    operations = "+-/*"
    expression = expression.replace(" ", "")

    return number


# tests
# expression = "10- 2- -5"
expression ="-7 * -(6 / 3)"

res = indexes(expression)
print(res)
