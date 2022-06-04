# Euler's method for a first-order ODE
# https://www.codewars.com/kata/56347fcfd086de8f11000014/train/python

import math


def func(x):
    return 1 + 0.5 * math.exp(-4 * x) - 0.5 * math.exp(-2 * x)


def ex_euler(n):
    error = 0
    h = 1 / n

    return error


res = ex_euler(10)
print(res)
