# https://github.com/Stxriboi/calculator--BC---IDK-
# Partner 1: Bryce Cephus
# Partner 2: Bryce Cephus

import math

# Required by autograder
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def exp(x, y):
    return x ** y

def mod(x, y):
    return x % y

def logarithm(x, base):
    return math.log(x, base)

def hypotenuse(a, b):
    return math.hypot(a, b)

def square_root(x):
    return math.sqrt(x)

# Required by your test_calculator.py
def subtract(x, y):
    return sub(x, y)

def multiply(x, y):
    return mul(x, y)

def divide(x, y):
    return div(x, y)

def power(x, y):
    return exp(x, y)
