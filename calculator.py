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
    import math
    return math.log(x, base)

def hypotenuse(a, b):
    import math
    return math.hypot(a, b)

def square_root(x):
    import math
    return math.sqrt(x)
