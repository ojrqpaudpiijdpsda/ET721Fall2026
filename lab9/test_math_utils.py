'''
Jiaxi Pang
Oct 5, 2026
Lab 9, unit testing using pytest
'''

import pytest
from math_utils import *

def test_multiply():
    assert multiply(3, 4) == 12
def test_divide():
    assert divide(10, 2) == 5
    # with tolerance up to two decimal places 
    assert divide(10,3) == pytest.approx(3.33, abs = 0.01)
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

#exercise 2



def test_valid_password():
    assert validate_password("pass1234") is True
def test_short_password():
    assert validate_password("pass1") is False
def test_no_number():
    assert validate_password("testingpassword") is False

#exercise 3
@pytest.mark.parametrize(
    "n, expected",
    [
        (2, True),
        (3, False),
        (0, True),
        (-2, True),
        (7, False),
    ]
)

def test_is_even(n, expected):
    assert is_even(n) == expected

@pytest.mark.parametrize(
    'password, expected',
    [
        ('pass1234', True),
        ('pass1', False),
        ('testingpassword', False),
        
    ]
)

def test_password(password, expected):
    assert validate_password(password) == expected