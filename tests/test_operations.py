from src.math_operations import add, sub, mul, div, mod, exp

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 0) == 0
    assert sub(-1, -1) == 0

def test_mul():
    assert mul(2, 3) == 6
    assert mul(-1, 1) == -1
    assert mul(0, 5) == 0

def test_div():
    assert div(6, 3) == 2
    assert div(-4, 2) == -2
    assert div(5, 2) == 2.5

def test_mod():
    assert mod(5, 3) == 2
    assert mod(10, 2) == 0
    assert mod(7, 4) == 3

def test_exp():
    assert exp(2, 3) == 8
    assert exp(3, 2) == 9
    assert exp(5, 0) == 1



