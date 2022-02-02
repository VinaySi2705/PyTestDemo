import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


"""
    fixtures as test is being broken down into 4 steps :
    1.> Arrange
    2.> Act
    3.> Assert
    4.> Cleanup
"""
# Through fixtures we take care of arrange and cleanup
driver = None

@pytest.fixture
def setup():
    print("Start Browser")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()
    print("close Browser")

def test_1(setup):
    driver.get("https://github.com/")
    print("Test 1 Executed")

def test_2(setup):
    driver.get("https://fast.com/")
    print("Test 2 Executed")

def test_3(setup):
    driver.get("https://www.youtube.com/")
    print('Test 3 Executed')
