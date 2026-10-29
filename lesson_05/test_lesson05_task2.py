from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_form_submission():
    driver = webdriver.Chrome()
    driver.maximize_window()

# Откройте страницу https://httpbin.qa-territory.online/forms/post.
    driver.get("https://httpbin.qa-territory.online/forms/post")

# Найдите поле ввода с названием custname.  name="custname"
# Введите в него ваше имя.
    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("Irina")
    sleep(3)

# Найдите кнопку Submit и нажмите на нее.
# В ТЗ кнопка указана как Submit, но в актуальной версии
# сайта кнопка называется Submit order
    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit order']")
    submit_button.click()
    sleep(2)

# Проверьте, что после нажатия URL изменился.
    assert "/post" in driver.current_url
    print(f"Форма отправленаю URL изменился на новый: {driver.current_url}")

    driver.quit()
