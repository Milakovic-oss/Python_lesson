from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()

# Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2.
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    wait = WebDriverWait(driver, 10)

# Найдите и нажмите на кнопку Start.
    start_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#start > button")
    ))
    start_button.click()

# Дождитесь появления текста Hello World!
    hello_element = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#finish h4")
        ))

# Сделайте скриншот страницы.
    driver.save_screenshot("screenshots/screen_hello_world.png")

# Проверьте, что появившийся текст равен Hello World!
    assert hello_element.text == "Hello World!"
    print("Тест пройден успешно!")

    driver.quit()
