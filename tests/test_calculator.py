import pytest
import sys
sys.path.insert(0, '.')
from src.calculator import add, subtract, multiply, is_even, factorial

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(3, 4) == 12  # Will fail — bug returns string

def test_is_even():
    assert is_even(4) == True   # Will fail — logic inverted
    assert is_even(3) == False

def test_factorial():
    assert factorial(5) == 120
