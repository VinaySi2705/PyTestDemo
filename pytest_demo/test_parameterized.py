import pytest

# Here we parametrize the input x,y and z with the below two values
@pytest.mark.parametrize("x,y,z",[(10,20,200),(20,40,200)])
def test_method(x,y,z):
    assert x*y == z
