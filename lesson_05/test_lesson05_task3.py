from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.maximize_window()

# Откройте страницу https://httpbin.qa-territory.online/links/10.
    driver.get("https://httpbin.qa-territory.online/links/10")

# Найдите все ссылки на странице (тег <a>).

    links_on_the_page = driver.find_elements(By.TAG_NAME, "a")

# Проверьте, что количество ссылок равно 9.
    assert len(links_on_the_page) == 9
    print(f"Найдено ровно {len(links_on_the_page)} ссылок")

# Проверьте, что все ссылки отображаются на странице.
    for link in links_on_the_page:
        assert link.is_displayed()
    print("Все ссылки видны на странице!")

# Проверьте, что текст первой ссылки содержит "1"
    first_link_text = links_on_the_page[0].text
    assert "1" in first_link_text
    print(f"Успешно! текст первой ссылки: '{first_link_text}'")

    driver.quit()
