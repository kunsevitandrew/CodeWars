# Calculating with Functions

dct = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def zero(res=()):  # your code here
    number = dct[zero.__name__]
    if len(res) == 0:
        return number
    if res[1] == "+":
        return number + res[0]
    if res[1] == "-":
        return number - res[0]
    if res[1] == "*":
        return number * res[0]
    if res[1] == "/":
        return number // res[0]


def one(res=()):  # your code here
    number = dct[one.__name__]
    if len(res) == 0:
        return number
    if res[1] == "+":
        return number + res[0]
    if res[1] == "-":
        return number - res[0]
    if res[1] == "*":
        return number * res[0]
    if res[1] == "/":
        return number // res[0]


def two(res=()):  # your code here
    number = dct[two.__name__]
    if len(res) == 0:
        return number
    if res[1] == "+":
        return number + res[0]
    if res[1] == "-":
        return number - res[0]
    if res[1] == "*":
        return number * res[0]
    if res[1] == "/":
        return number // res[0]


def three(res=()):  # your code here
    number = dct[three.__name__]
    if len(res) == 0:
        return number
    if res[1] == "+":
        return number + res[0]
    if res[1] == "-":
        return number - res[0]
    if res[1] == "*":
        return number * res[0]
    if res[1] == "/":
        return number // res[0]


def four(res=()):  # your code here
    number = dct[four.__name__]
    if len(res) == 0:
        return number
    if res[1] == "+":
        return number + res[0]
    if res[1] == "-":
        return number - res[0]
    if res[1] == "*":
        return number * res[0]
    if res[1] == "/":
        return number // res[0]


def five(res=()):  # your code here
    number = dct[five.__name__]
    if len(res) == 0:
        return number
    if res[1] == "+":
        return number + res[0]
    if res[1] == "-":
        return number - res[0]
    if res[1] == "*":
        return number * res[0]
    if res[1] == "/":
        return number // res[0]


def six(res=()):  # your code here
    number = dct[six.__name__]
    if len(res) == 0:
        return number
    if res[1] == "+":
        return number + res[0]
    if res[1] == "-":
        return number - res[0]
    if res[1] == "*":
        return number * res[0]
    if res[1] == "/":
        return number // res[0]


def seven(res=()):  # your code here
    number = dct[seven.__name__]
    if len(res) == 0:
        return number
    if res[1] == "+":
        return number + res[0]
    if res[1] == "-":
        return number - res[0]
    if res[1] == "*":
        return number * res[0]
    if res[1] == "/":
        return number // res[0]


def eight(res=()):  # your code here
    number = dct[eight.__name__]
    if len(res) == 0:
        return number
    if res[1] == "+":
        return number + res[0]
    if res[1] == "-":
        return number - res[0]
    if res[1] == "*":
        return number * res[0]
    if res[1] == "/":
        return number // res[0]


def nine(res=()):  # your code here
    number = dct[nine.__name__]
    if len(res) == 0:
        return number
    if res[1] == "+":
        return number + res[0]
    if res[1] == "-":
        return number - res[0]
    if res[1] == "*":
        return number * res[0]
    if res[1] == "/":
        return number // res[0]


def plus(func):  # your code here
    return (func, "+")


def minus(func):  # your code here
    return (func, "-")


def times(func):  # your code here
    return (func, "*")


def divided_by(func):  # your code here
    return (func, "/")


res = zero(minus(one()))
print(res)


# other variants:
# 1)
# def zero(f = None): return 0 if not f else f(0)
# def one(f = None): return 1 if not f else f(1)
# def two(f = None): return 2 if not f else f(2)
# def three(f = None): return 3 if not f else f(3)
# def four(f = None): return 4 if not f else f(4)
# def five(f = None): return 5 if not f else f(5)
# def six(f = None): return 6 if not f else f(6)
# def seven(f = None): return 7 if not f else f(7)
# def eight(f = None): return 8 if not f else f(8)
# def nine(f = None): return 9 if not f else f(9)
#
# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda  x: x*y
# def divided_by(y): return lambda  x: x/y

# 2)
# id_ = lambda x: x
# number = lambda x: lambda f=id_: f(x)
# zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
# plus = lambda x: lambda y: y + x
# minus = lambda x: lambda y: y - x
# times = lambda x: lambda y: y * x
# divided_by = lambda x: lambda y: y / x