import pytest
from utils.helpers import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
    