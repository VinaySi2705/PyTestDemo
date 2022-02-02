# In this we are gonna use all inbuilt markers
import pytest
import sys


# Below is unconditional skip
@pytest.mark.skip
def test_login():
    print("login done")


# Below is conditional skip
@pytest.mark.skipif(sys.version_info<(3,10),reason="Python version not supported")
def test_addPro():
    print("add products")

@pytest.mark.xfail
def test_logout():
    assert False
    print('Logout Done')


def test_closeApplication():
    assert True
    print("close the application")
