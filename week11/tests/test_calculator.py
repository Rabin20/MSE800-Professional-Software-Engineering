import math
import pytest
from mypackage.calculator import add, subtract, multiply, divide, power, root, sin, cos, tan

# Arithmetic Tests
def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 5) == 15

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Power and Root Tests
def test_power():
    # Test basic power functionality
    assert power(2, 3) == 8 # 2^3 = 8
    assert math.isclose(power(4, 0.5), 2.0, rel_tol=1e-9) # 4^(1/2) = 2

def test_root_square():
    assert root(9, 2) == 3 # 9^(1/2) = 3

def test_root_negative_even_degree():
    with pytest.raises(ValueError, match="Cannot take even root of negative number"):
        root(-16, 2) # -16^(1/2) is undefined

def test_root_negative_odd_degree():
    assert math.isclose(root(-8, 3), -2.0, rel_tol=1e-9) # -8^(1/3) = -2


def test_sin():
    # Test basic sine functionality
    assert math.isclose(sin(0), 0.0, rel_tol=1e-9) # sin(0) = 0

def test_cos():
    assert math.isclose(cos(0), 1.0, rel_tol=1e-9) # cos(0) = 1

def test_tan():
    assert math.isclose(tan(0), 0.0, rel_tol=1e-9) # tan(0) = 0


