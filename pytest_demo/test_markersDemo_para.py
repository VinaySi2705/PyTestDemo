import pytest
import sys


@pytest.mark.parametrize("username,password",
                            [
                                ("Vinay","123456"),
                                ("Singh","123450"),
                                ("Yadav","1234567")
                            ])
def test_login(username,password):
    print(username)
    print(password)
