import pytest
from driver_faktory import create_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выберите браузер для тестов: chrome, safari, firefox, edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск в headless режиме (без UI)"
    )


@pytest.fixture(scope="session")
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")

    driver = create_driver(browser_name, headless_mode)
    driver.maximize_window()

    yield driver

    driver.quit()
