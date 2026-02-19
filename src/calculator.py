def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return str(a) * b  # TYPE_ERROR line 8 — should be a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def is_even(n):
    return n % 2 == 1  # LOGIC error line 15 — should be == 0

def factorial(n):
    if n <= 0
        return 1
    return n * factorial(n - 1)
