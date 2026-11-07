from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

# Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")

# Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZGZmZTYwZTAtZGMwYy00Y2MwLWE2ZjgtMjE5NDZjM2E5MmE2",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

# Обновите страницу.
    driver.refresh()

# Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/ozzz")

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".user-profile__username")
    ))

# Сохраните текущий URL.
    url_user_1 = driver.current_url
    print(f"URL Пользователя 1: {url_user_1}")

# Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()

# Установите cookie пользователя 2.
    driver.add_cookie({
        "name": "SESSION",
        "value": "NTcwMjk5ZTctYTQyZS00YjkzLTk3MDMtMWM3ODU5ZGJkM2I3",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })
# Обновите страницу.
    driver.refresh()

# Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/zfm")

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".user-profile__username")
    ))

# Сохраните текущий URL.
    url_user_2 = driver.current_url
    print(f"URL Пользователя 2: {url_user_2}")

# Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user_1 != url_user_2
    print("Тест пройден успешно: URL пользователей отличаются!")

    driver.quit()
