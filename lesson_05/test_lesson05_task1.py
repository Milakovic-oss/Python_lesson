from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_navigation():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Откройте страницу https://httpbin.qa-territory.online.
    driver.get("https://httpbin.qa-territory.online/")
    sleep(3)

    # Найдите и кликните на ссылку HTML Form.
    html_form_button = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_button.click()
    sleep(3)

    # Проверьте, что URL изменился на /forms/post.
    assert "/forms/post" in driver.current_url
    print(driver.current_url)

    # Вернитесь назад на главную страницу.
    driver.back()
    sleep(2)

    # Проверьте, что вернулись на исходный URL
    assert driver.current_url == "https://httpbin.qa-territory.online/"
    print("Вернулись на главную страницу!")

    driver.quit()
