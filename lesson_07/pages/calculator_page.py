from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get("https://bonigarcia.dev/"
                        "selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, value):
        # метод для ввода задержки
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(value))

    def click_button(self, button_text):
        # метод для нажатия на любую кнопку калькулятора (7, +, 8, =)
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_result(self):
        # метод для получения текста с экрана
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text

    def wait_for_result(self, expected_text, timeout=60):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected_text)
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
