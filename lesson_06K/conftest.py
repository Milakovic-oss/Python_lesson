import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Выберите браузер: chrome, firefox или edge"
    )


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise pytest.UsageError(f"Неподдерживаемый браузер: {browser}")

    driver.maximize_window()

    yield driver

    driver.quit()
