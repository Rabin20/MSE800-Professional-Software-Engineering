import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b): return a ** b
def root(a, n):
    if a < 0 and n % 2 == 1:
        return - (abs(a) ** (1 / n))
    elif a < 0 and n % 2 == 0:
        raise ValueError("Cannot take even root of negative number")
    else:
        return a ** (1 / n)


def sin(x): return math.sin(x)
def cos(x): return math.cos(x)
def tan(x):
    if math.isclose(math.cos(x), 0.0, abs_tol=1e-9):
        raise ValueError("tan is undefined for this input")
    return math.tan(x)