from selenium import webdriver


def create_driver(browser="chrome", headless=False):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(60)
        return driver

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        return driver

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(options=options)
        return driver

    elif browser == "safari":
        if headless:
            raise ValueError("Опция не поддерживается")
        return webdriver.Safari()
    else:
        raise ValueError(f"Браузер {browser} не поддерживается")
