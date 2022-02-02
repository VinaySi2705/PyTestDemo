import pytest

def func(x):
    return x + 5

def test_1():
    assert func(3) == 8

def test_2():
    name = "Vinay"
    title = "Vinay is a student"
    assert name is title , "Title does not match"
    #after assert argument only printed if test is false
    
